'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input("Informe M ou F: ")
letra = letra.lower()

if letra == "m":
    print("M - masculino")
elif letra == "f":
    print("F - feminino")
else:
    print("Sexo inválido.")