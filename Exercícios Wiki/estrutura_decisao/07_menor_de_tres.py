'''
Faça um Programa que leia três números e mostre o maior e o menor deles. 
'''

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f"Menor: {menor}")


lista = [n1, n2, n3]
lista.sort()
print(f"Lista em ordem crescente: {lista}")