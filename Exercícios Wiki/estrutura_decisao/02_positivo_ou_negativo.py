'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
'''

valor = float(input("Informe um número: "))
if valor == 0:
    print('''O valor é zero. Nem positivo, nem negativo. De acordo com o Wikipedia, 
o zero não é um número positivo nem negativo, já que não é maior nem menor que si mesmo.''')
elif valor > 0:
    print("Número positivo.")
else:
    print("Número negativo.")