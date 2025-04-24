import pandas as pd

# Lê o arquivo CSV em um DataFrame do pandas
df = pd.read_csv('Pasta1.CSV')

# Cria um dicionário com as abas e seus respectivos dados
abas = {'Fundo01': df.iloc[:100000], 'Fundo02': df.iloc[100001:200000], 'Fundo03': df.iloc[200001:300000], 'Fundo04': df.iloc[300001:400000], 'Fundo05': df.iloc[400001:500000], 'Fundo06': df.iloc[500001:600000]}

# Cria um arquivo Excel e adiciona as abas ao arquivo
with pd.ExcelWriter('arquivo_excel.xlsx') as writer:
    for aba, dados in abas.items():
        dados.to_excel(writer, sheet_name=aba, index=False)