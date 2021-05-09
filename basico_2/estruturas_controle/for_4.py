from random import randint


def sortear_dado():
    return randint(1, 6)

for numero in range(1, 7):
    if numero % 2 == 1:
        continue

    if sortear_dado() == numero:
        print('Acertou! ',numero)
        break
