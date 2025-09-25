import pandas as pd
# carregar planilha do excel
try:
    df=pd.read_excel('vendas.xlsx')
except FileNotFoundError:
    print("Planilha não encontrada.")
    exit()