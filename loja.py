import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# carregar planilha do excel
try:
    df=pd.read_excel('vendas.xlsx')
    #df=pd.read_csv('vendas.csv')
except FileNotFoundError:
    print("Planilha não encontrada.")
    exit()

print(df)
#Análise exploratória
df['total_vendas']=df['quantidade']*df['valor']
#agrupar os dados por jogo e somar
vendas_por_jogo=df.groupby('jogo')['total_vendas'].sum().reset_index()
print("Total vendas por jogo: ",vendas_por_jogo)
#Visualização das vendas
#Criação de um gráfico
plt.figure(figsize=(10,6))
plt.bar(vendas_por_jogo['jogo'],vendas_por_jogo['total_vendas'],color='blue')
plt.title('Total de vendas por jogo')
plt.xlabel('Jogo')
plt.ylabel('Total de Vendas R$')
plt.xticks(rotation=45)
plt.grid(axis='y',linestyle='--')
plt.tight_layout()
plt.show()

