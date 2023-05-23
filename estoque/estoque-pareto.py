import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
df = pd.read_excel('PlanilhaPadrao_B2BX_ESTOQUE.xls', header=0)

# Convertendo os nomes das colunas para minúsculas
df.columns = map(str.lower, df.columns)

# Convertendo os valores da coluna CURVA para strings
df['curva'] = df['curva'].astype(str)

# Agrupando os valores da coluna CURVA e somando os valores da coluna Estoque
df_grouped = df.groupby('curva')['estoque'].sum().reset_index()

# Ordenando o DataFrame com base na coluna Estoque em ordem decrescente
df_grouped = df_grouped.sort_values(by=['estoque'], ascending=False)

# Calculando a porcentagem acumulada da coluna Estoque
df_grouped['porcentagem_acumulada'] = (df_grouped['estoque'].cumsum() / df_grouped['estoque'].sum()) * 100

# Criando o gráfico de Pareto
fig, ax1 = plt.subplots()

# Adicionando o valor da coluna Estoque em cima de cada coluna
for i, v in enumerate(df_grouped['estoque']):
    ax1.annotate(str(v), xy=(i+0.5, v), ha='center', va='bottom')

ax1.bar(df_grouped['curva'], df_grouped['estoque'], color='tab:blue')
ax1.set_xlabel('CURVA')
ax1.set_ylabel('Estoque', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()

ax2.plot(df_grouped['curva'], df_grouped['porcentagem_acumulada'], color='tab:red', marker='o')
ax2.set_ylabel('Porcentagem Acumulada', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title('Gráfico de Pareto de Estoque')

plt.show()