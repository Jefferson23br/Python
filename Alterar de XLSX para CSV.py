
import os
import pandas as pd

# Define o diretório com os arquivos XLSX
diretorio_xlsx = r'caminho do diretorio'

# Define o diretório para salvar os arquivos CSV
diretorio_csv = r'caminho aonde salvar'

# Percorre todos os arquivos XLSX no diretório
for nome_arquivo in os.listdir(diretorio_xlsx):
    if nome_arquivo.endswith('.xlsx'):
        # Carrega o arquivo XLSX em um DataFrame do Pandas
        caminho_arquivo_xlsx = os.path.join(diretorio_xlsx, nome_arquivo)
        df = pd.read_excel(caminho_arquivo_xlsx)

        # Salva o DataFrame em um arquivo CSV
        nome_arquivo_csv = nome_arquivo[:-5] + '.csv'  # remove a extensão .xlsx e adiciona a extensão .csv
        caminho_arquivo_csv = os.path.join(diretorio_csv, nome_arquivo_csv)
        df.to_csv(caminho_arquivo_csv, index=False)
