import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
df = pd.read_excel('PlanilhaPadrao_B2BX_ESTOQUE.xls', header=0)

# Convertendo os nomes das colunas para minúsculas
df.columns = map(str.lower, df.columns)

# Convertendo os valores da coluna TÍTULO para strings
df['título'] = df['título'].astype(str)

# Ordenando o DataFrame com base na coluna Estoque em ordem crescente
df = df.sort_values(by=['estoque'])

# Criando o gráfico de dispersão
for i in range(len(df)):
    plt.scatter(df['título'][i], df['estoque'][i])
    plt.annotate(df['título'][i], (df['título'][i], df['estoque'][i]))

# Adicionando um título ao gráfico
plt.title('Gráfico de Dispersão de Estoque')

# Adicionando rótulos aos eixos x e y
plt.xlabel('TÍTULO')
plt.ylabel('Estoque')

# Exibindo o gráfico
plt.show()