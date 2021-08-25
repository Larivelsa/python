'''
Faça um programa que pergunte o preço de três 
produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''


p1 = float(input("Informe o primeiro preço: "))
p2 = float(input("Informe o segundo preço: "))
p3 = float(input("Informe o terceiro preço: "))

menor = p1

if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3
print(f"Mais barato: R$ {menor:.2f}")