from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def ajuda(script):
    print("É necessário informar o raio do círculo.")
    print(f"Sintaxe: {script} <raio>")


if __name__ == '__main__':

    if len(sys.argv) < 2:
        ajuda(sys.argv[0])
        sys.exit(errno.EPERM)

    elif not sys.argv[1].isnumeric():
        ajuda(sys.argv[0])
        print(TerminalColor.ERRO, 'O raio deve ser numérico',
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(f'A área da circunferência é de {area}')
