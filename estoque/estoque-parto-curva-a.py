import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
df = pd.read_excel('PlanilhaPadrao_B2BX_ESTOQUE.xls', header=0)

# Convertendo os nomes das colunas para minúsculas
df.columns = map(str.lower, df.columns)

# Filtrando os valores da coluna CURVA que são iguais a "A"
df_a = df[df['curva'] == 'A']

# Agrupando os valores da coluna TÍTULO e somando os valores da coluna Estoque
df_grouped = df_a.groupby('título')['estoque'].sum().reset_index()

# Ordenando o DataFrame com base na coluna Estoque em ordem decrescente
df_grouped = df_grouped.sort_values(by=['estoque'], ascending=False)

# Calculando a porcentagem acumulada da coluna Estoque
df_grouped['porcentagem_acumulada'] = (df_grouped['estoque'].cumsum() / df_grouped['estoque'].sum()) * 100

# Criando o gráfico de Pareto
fig, ax1 = plt.subplots()

ax1.bar(df_grouped['título'], df_grouped['estoque'], color='tab:blue')
ax1.set_xlabel('TÍTULO')
ax1.set_ylabel('Estoque', color='tab:blue')

# Adicionando o valor da coluna Estoque em cima de cada coluna
for i, v in enumerate(df_grouped['estoque']):
    ax1.annotate(str(v), xy=(i+0.5, v), ha='center', va='bottom')

# Quebrando os rótulos da coluna TÍTULO em duas linhas
ax1.set_xticklabels([x.replace(' ', '\n') for x in df_grouped['título']], rotation=90)

# Criando o eixo secundário para a porcentagem acumulada
ax2 = ax1.twinx()
ax2.plot(df_grouped['título'], df_grouped['porcentagem_acumulada'], color='tab:red', marker='o')
ax2.set_ylabel('Porcentagem Acumulada', color='tab:red')
ax2.set_ylim([0, 110])

plt.show()