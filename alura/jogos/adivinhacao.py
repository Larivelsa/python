import random


def jogar():
    print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
    print("*  Bem vinda ao jogo de adivinhação *")
    print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    nivel = int(input('''Qual o nível de dificuldade? 
    (1) Fácil - (2) Médio - (3) Difícil: \n'''))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        chute = int(input("Digite seu número: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # continua o laço for

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if (maior):
                print("Você errou. Seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou. Seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo.")


if(__name__ == "__main__"):
    jogar()
