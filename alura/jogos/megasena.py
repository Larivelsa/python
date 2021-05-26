# gerar conjunto de jogos
import random
fixos = (12, 53, 56, 33)


numero_jogos = 3
while numero_jogos > 0:

    jogo = list(fixos)
    jogo.append(random.randrange(1, 61))
    jogo.append(random.randrange(1, 61))
    jogo.sort()
    print(jogo)
    print('------------------------')

    numero_jogos -= 1


# fix: problema com números repetidos
