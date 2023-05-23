import openai
import os

# Define a chave de API da OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a mensagem de boas-vindas
mensagem = "Olá, sou o Emojitron da DarkSide Books, a primeira editora brasileira dedicada ao terror, à magia e ao True Crime. Digite o nome de um filme que vou traduzi-lo pra você na linguagem dos emojis :)))"

# Imprime a mensagem de boas-vindas
print(mensagem)

# Loop principal do programa
while True:
    # Lê o nome do filme digitado pelo usuário
    nome_filme = input("> ")

    # Define o prompt para a geração de emojis
    prompt = f"Traduza o nome do filme '{nome_filme}' para emojis."

    # Define os parâmetros da solicitação de geração de texto
    model_engine = "text-davinci-002"
    temperature = 0.5
    max_tokens = 50

    # Envia a solicitação de geração de texto para a API da OpenAI
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Extrai a resposta da API da OpenAI
    emojis = response.choices[0].text.strip()

    # Verifica se a resposta é vazia ou contém apenas espaços em branco
    if not emojis:
        # Responde ao usuário com uma mensagem de erro
        print("Desculpe, isto não me parece como um nome de filme conhecido. Sou um Emojitron, só sei gerar emojis baseados em nomes de filmes! Tente novamente.")
    else:
        # Imprime a resposta em emojis
        print(emojis)