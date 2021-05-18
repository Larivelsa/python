print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
print("*  Bem vinda ao jogo de adivinhação *")
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")

numero_secreto = 42
total_tentativas = 3
rodada = 1


while(rodada <= total_tentativas > 0):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite seu número: "))

    print(f"Você digitou {chute}")

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou. Seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou. Seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo.")
