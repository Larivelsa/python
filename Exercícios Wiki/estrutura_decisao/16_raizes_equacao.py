'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não 
    deve fazer pedir os demais valores, sendo encerrado;

    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 

Fórmula para calcula delta: delta = b2 – 4ac
'''
import math

a = float(input('Informe o valor de a: '))
if a <= 0:
    print('Valor de a menor ou igual a 0.')
    exit()

b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = b**2 - 4*a*c


if delta < 0:
    resultado_raiz = None
    print(f'Equação não possui raízes reais.')

elif delta == 0:
    resultado_raiz = math.sqrt(delta)
    x = -b/(2*a)
    print(f'Delta: {resultado_raiz}')
    print(f'Equação possui apenas uma raíz: {x:.2f}')

else:
    resultado_raiz = math.sqrt(delta)
    x1 = (-b+(resultado_raiz))/(2*a)
    x2 = (-b-(resultado_raiz))/(2*a)
    print(f'Equação possui duas raízes, sendo x\': {x1:.2f} e x\'\': {x2:.2f}')
