import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Criar pasta de resultados se não existir
output_dir = "resultados"
os.makedirs(output_dir, exist_ok=True)

# Ler a lista de ações
acoes_df = pd.read_csv('acoes.csv')
acoes = acoes_df['ticker'].tolist()

# Datas
end_date = pd.to_datetime('today')
start_date = end_date - pd.DateOffset(months=24)

# Armazenamento
dados_acoes = {}
acoes_com_erro = []
acoes_oportunidades = []  # Armazenar informações das ações com oportunidade de compra

# Coletar dados
for ticker in acoes:
    print(f'Buscando dados para {ticker}')
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            df['Max_Hist'] = df['High'].cummax()
            df['Min_Hist'] = df['Low'].cummin()
            dados_acoes[ticker] = df
        else:
            print(f'Nenhum dado para {ticker}')
            acoes_com_erro.append(ticker)
    except Exception as e:
        print(f'Erro com {ticker}: {e}')
        acoes_com_erro.append(ticker)

# Plot gráfico das ações com preço <= 70% da máxima histórica
plt.figure(figsize=(14, 8))
cores = plt.cm.get_cmap('tab10', len(dados_acoes))
plotted = 0

for i, (ticker, df) in enumerate(dados_acoes.items()):
    preco_atual = df['Close'].iloc[-1]  # Garantir que é o valor único
    max_historico = df['Max_Hist'].iloc[-1]  # Garantir que é o valor único
    
    # Garantir que estamos comparando valores escalares
    preco_atual = preco_atual.item()  # Convertendo para valor escalar
    max_historico = max_historico.item()  # Convertendo para valor escalar
    
    # Verificar se o preço atual está <= 70% da máxima histórica
    if preco_atual <= 0.7 * max_historico:
        plt.plot(df.index, df['Close'], label=ticker, color=cores(i))
        plt.scatter(df.index[-1], preco_atual, color=cores(i))
        plt.annotate(f'{ticker}\n{preco_atual:.2f}',
                     (df.index[-1], preco_atual),
                     textcoords="offset points",
                     xytext=(0,10),
                     ha='center',
                     color=cores(i))
        
        # Adicionar as informações da ação com oportunidade de compra na lista
        acoes_oportunidades.append({
            'Ticker': ticker,
            'Preço Atual': preco_atual,
            'Máxima Histórica': max_historico
        })
        plotted += 1

# Se tiver algum gráfico plotado, salvar
if plotted > 0:
    plt.title('Ações com preço atual <= 70% da máxima histórica')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'oportunidades_precos_baixos.png'))
    print('Gráfico salvo em:', os.path.join(output_dir, 'oportunidades_precos_baixos.png'))
else:
    print('Nenhuma ação atende ao critério para o gráfico.')

# Gerar arquivo Excel com as ações que atendem ao critério
if acoes_oportunidades:
    df_oportunidades = pd.DataFrame(acoes_oportunidades)
    excel_file = os.path.join(output_dir, 'oportunidades_precos_baixos.xlsx')
    df_oportunidades.to_excel(excel_file, index=False)
    print(f'Excel gerado: {excel_file}')

# Exibir ações com erro
if acoes_com_erro:
    print('\nAções com erro ou sem dados:')
    for acao in acoes_com_erro:
        print('-', acao)
