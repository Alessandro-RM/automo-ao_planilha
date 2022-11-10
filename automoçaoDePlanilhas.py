import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'planilha_venda1.xlsx'
arquivo_excel_2 = 'planilha_venda3.xlsx'

#ler os arquivos e joga
df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='dia1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='dia2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

# consolidar os dataFrames
df_todas_as_planilhas = pd.concat([df_dia_1, df_dia_2, df_dia_3])

#soma de lucro
lucro_vendedores = df_todas_as_planilhas.groupby(['VENDEDOR']).sum()

relatorio_final = lucro_vendedores.loc[:, "UNIDADES":"PREÇO"]

#Grafico de vendas
relatorio_final.plot(kind='bar')

plt.show()