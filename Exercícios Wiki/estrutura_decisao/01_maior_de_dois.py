'''
Faça um Programa que peça dois números e imprima o maior deles.
'''
a = float(input("Informe um número: "))
b = float(input("Informe outro número: "))

if a == b:
    print("Os dois números são iguais.")
elif a > b:
    print("O primeiro número é maior do que o segundo.")
else:
    print("O segundo número é maior do que o primeiro número.")
    