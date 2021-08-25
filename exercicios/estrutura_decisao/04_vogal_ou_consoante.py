'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input("Digite uma letra: ")
vogais = ['a','e','i','o','u']

if letra.lower() in vogais:
    print(f"A letra {letra} é uma vogal.")
else:
    print(f"A letra {letra} não é uma vogal.")
