import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
df = pd.read_excel('PlanilhaPadrao_B2BX_ESTOQUE.xls', header=0)

# Filtrando os valores da coluna SELO que são iguais a "Graphic Novel"
df_gn = df[df['SELO'] == 'Graphic Novel']

# Agrupando as quantidades pelo campo TÍTULO e ordenando em ordem decrescente
grouped = df_gn.groupby('TÍTULO')['Estoque'].sum().sort_values(ascending=False)

# Criando o gráfico de colunas com uma área maior
fig, ax = plt.subplots(figsize=(10, 6))
grouped.plot(kind='bar', color='red', ax=ax)

# Adicionando um título ao gráfico
ax.set_title('Estoque por Título (Graphic Novel)')

# Adicionando rótulos aos eixos x e y
ax.set_xlabel('Título')
ax.set_ylabel('Estoque')

# Exibindo os rótulos do título na horizontal e diminuindo a fonte
plt.xticks(rotation=90, fontsize=8)

# Adicionando rótulos com a quantidade de cada coluna
for i in ax.containers:
    ax.bar_label(i, label_type='edge', fontsize=10)

# Exibindo o gráfico com a margem branca diminuída
plt.tight_layout()
plt.show()