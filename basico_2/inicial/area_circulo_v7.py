from math import pi
import sys
import errno 

def circulo(raio):
    return pi * float(raio) ** 2

def ajuda(script):
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {script} <raio>")

if __name__ == '__main__':

    if len(sys.argv) < 2:
        ajuda(sys.argv[0])
        #sys.exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f'A área da circunferência é de {area}')
