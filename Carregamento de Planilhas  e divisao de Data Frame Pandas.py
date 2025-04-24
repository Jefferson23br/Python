import pandas as pd
import glob
import xlsxwriter

file_list = glob.glob("*.csv")

df_list = []
for filename in file_list:
    df = pd.read_csv(filename)
    df_list.append(df)

df = pd.concat(df_list, axis=0, ignore_index=True)

linhas_por_aba = 10

lista_de_abas = [df[i:i+linhas_por_aba] for i in range(0, len(df), linhas_por_aba)]

writer = pd.ExcelWriter('Nova.xlsx', engine='xlsxwriter')

for i, df_aba in enumerate(lista_de_abas):
    df_aba.to_excel(writer, sheet_name=f'Aba{i+1}', index=False)

writer.save()