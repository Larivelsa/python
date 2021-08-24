# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

inteiro_1 = int(input("Informe um número inteiro: "))
inteiro_2 = int(input("Informe outro número inteiro: "))
real = float(input("Informe um número real: "))

# - o produto do dobro do primeiro com metade do segundo.
produto = inteiro_1 * 2 + inteiro_2 / 2

# - a soma do triplo do primeiro com o terceiro.
soma = inteiro_1 * 3 + real

# - o terceiro elevado ao cubo.
cubo = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é {produto:.2f}")
print(f"A soma do triplo do primeiro com o terceiro é {soma:.2f}")
print(f"O terceiro elevado ao cubo {cubo:.2f}")
