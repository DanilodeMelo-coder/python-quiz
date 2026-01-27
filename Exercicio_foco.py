
quiz = [
    {
    'Pergunta': 'Qual linguagem é mais usada para ciência de dados?',
    'Opções': ['Java', 'Python', 'C', 'PHP'],
    'Resposta': 'Python',
    },

    {
    'Pergunta': 'Qual estrutura de dados armazena pares chave-valor em Python?',
    'Opções': ['Lista', 'Tupla', 'Dicionário', 'Conjunto'],
    'Resposta': 'Dicionário',
    },

]

acertos = 0

for pergunta in quiz:
    print(pergunta["Pergunta"])

    for i, opcao in enumerate(pergunta["Opções"]):
        print(f"{i}) {opcao}")

    resposta_user = int(input("Escolha uma das alternativas: "))

    if resposta_user < 0 or resposta_user >= len(pergunta["Opções"]):
        print("Resposta invalida")
        continue

    if pergunta["Opções"][resposta_user] == pergunta["Resposta"]:
        print("Você acertou, parabéns!!!!")
        acertos += 1
    else:
        print("Você errou, que pena")

print(f"Você acertou {acertos} de {len(quiz)} perguntas")