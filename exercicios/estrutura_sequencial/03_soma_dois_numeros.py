# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# Separar a parte inteira da decimal e apresentar cada uma com cinco algorismos em cada parte
'''
n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
'''
import random


n1 = random.random()*10
n2 = random.random()*10

print("numero 1 ", n1)
print("numero 2 ", n2)

soma = n1+n2

parte_inteira = int(soma)
parte_decimal = soma - parte_inteira
string_parte_decimal = str(parte_decimal)
string_parte_decimal_removendo_o_zero = string_parte_decimal[2:7]
parte_decimal = int(string_parte_decimal_removendo_o_zero)
print(parte_decimal)

print(f"A soma dos números é {parte_inteira:4d},{parte_decimal}")
