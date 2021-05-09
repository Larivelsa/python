from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')

    area=circulo(raio)
    print(f'A área da circunferência é de {area}')
