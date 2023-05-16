import pandas as pd
import os
import matplotlib.pyplot as plt

# Lê o arquivo Excel em um DataFrame do pandas
df = pd.read_excel('emails.xlsx')

# Verifica se há endereços de email duplicados na coluna "EMAIL"
duplicatas = df[df.duplicated(['EMAIL'], keep=False)]

# Imprime os endereços de email duplicados
if not duplicatas.empty:
    print('Endereços de email duplicados encontrados:')
    print(duplicatas['EMAIL'].unique())
    print(f'Total de {len(duplicatas)} emails repetidos encontrados.')
else:
    print('Nenhum endereço de email duplicado encontrado.')

# Filtra os endereços de email duplicados na coluna "EMAIL"
df_filtrado = df.drop_duplicates(subset=['EMAIL'])

# Verifica se o arquivo "clean-emails.xlsx" já existe e o exclui, se necessário
if os.path.exists('clean-emails.xlsx'):
    os.remove('clean-emails.xlsx')

# Escreve os dados filtrados em um novo arquivo Excel
df_filtrado.to_excel('clean-emails.xlsx', index=False)

# Imprime uma mensagem para confirmar que o novo arquivo foi criado ou reescrito com sucesso
if os.path.exists('clean-emails.xlsx'):
    print('O arquivo "clean-emails.xlsx" foi reescrito com sucesso.')
else:
    print('Novo arquivo "clean-emails.xlsx" criado sem endereços de email duplicados.')

# Conta a quantidade de endereços de email por domínio
contagem = df_filtrado['EMAIL'].str.split('@', expand=True).iloc[:, 1].value_counts()

# Cria uma lista com os valores a serem exibidos no gráfico
valores = [len(df), len(df_filtrado)]

# Plota um gráfico de barras com a contagem de domínios de email e o total de registros
plt.barh(['Total de registros', 'Registros sem emails duplicados'], valores)
plt.title('Contagem de domínios de email')
plt.xlabel('Quantidade')
plt.ylabel('Tipo')
plt.gca().invert_yaxis()
plt.show()