import os
from time import sleep

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

def rodar_quiz():
    acertos = 0
    erros = 0

    for pergunta in quiz:
        print(pergunta["Pergunta"])

        for i, opcao in enumerate(pergunta["Opções"]):
            print(f"{i}) {opcao}")

        resposta_user = input("Escolha uma das alternativas: ")

        if resposta_user.isdigit() != True:
            print("Digite apenas numeros!!")
            continue
        else:
            resposta_user = int(resposta_user)

        if resposta_user < 0 or resposta_user >= len(pergunta["Opções"]):
            print("Resposta invalida")
            continue

        if pergunta["Opções"][resposta_user] == pergunta["Resposta"]:
            print("Você acertou, parabéns!!!!")
            acertos += 1
        else:
            print("Você errou, que pena")
            erros += 1

    porcentagem_final = (acertos/len(quiz)) * 100

    return acertos, erros, porcentagem_final

def menu_final(acertos, erros, porcentagem_final):
    print(f"Você acertou {acertos} de {len(quiz)} perguntas")
    print(f"Você errou {erros} de {len(quiz)} perguntas")
    print(f"Sua porcentagem final foi de {porcentagem_final}%")

def desempenho(porcentagem_final):
    if porcentagem_final >= 80:
        print(f"Parabéns, obteve um ótimo desempenho")
    elif porcentagem_final >= 50:
        print(f"Pode melhorar, obteve desempenho médio")
    else:
        print(f"Estude mais, você teve um desempenho ruim")

def sair_ou_continuar():
    sair_continuar = input("Deseja continuar? [S]im/[N]ão ")
    return sair_continuar.startswith("s") 

while True:
    acertos, erros, porcentagem_final = rodar_quiz()
    menu_final(acertos, erros, porcentagem_final)

    desempenho(porcentagem_final)

    if sair_ou_continuar() == True:
        print()
        acertos = 0
        erros = 0

        print("REINCIANDO PROGRAMA...")

        sleep(1.0)

        os.system("cls")

        continue

    else:
        print()

        print("ENCERRANDO PROGRAMA...")

        break


