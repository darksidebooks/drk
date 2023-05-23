import pandas as pd

# Lê o arquivo CSV em um DataFrame do pandas
df = pd.read_csv('MOBILE_COMPRADORES_DARKLOVE_OU_MAGICAE_20230317_154716.csv', delimiter='|')

# Filtra os registros que contêm os números de 2 a 5 no quinto algarismo da coluna TELEFONE e começam com 55
filtro = (df['TELEFONE'].astype(str).str[4].isin(['2', '3', '4', '5'])) & (df['TELEFONE'].astype(str).str.startswith('55'))
registros = df[filtro]

# Grava um novo arquivo CSV excluindo os registros encontrados
df_sem_registros = df[~filtro]
df_sem_registros.to_csv('clean-telefones-responsys.csv', sep='|', index=False)

# Imprime o total de registros encontrados e os chama de "TELEFONES FIXOS"
total_registros = len(registros)
print(f'Total de TELEFONES FIXOS encontrados: {total_registros}')