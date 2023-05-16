import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
df = pd.read_excel('PlanilhaPadrao_B2BX_ESTOQUE.xls', header=0)

# Agrupando as quantidades pelo campo selo
grouped = df.groupby('SELO')['Estoque'].sum()

# Criando o gráfico de colunas
ax = grouped.plot(kind='bar', color='red')

# Adicionando um título ao gráfico
ax.set_title('Estoque por Selo')

# Adicionando rótulos aos eixos x e y
ax.set_xlabel('Selo')
ax.set_ylabel('Estoque')

# Exibindo os rótulos do selo na horizontal
plt.xticks(rotation=0)

# Adicionando rótulos com a quantidade de cada coluna
for i in ax.containers:
    ax.bar_label(i, label_type='edge', fontsize=10)

# Exibindo o gráfico
plt.show()