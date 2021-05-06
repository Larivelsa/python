from calculadora import Calculadora
from comodo import Comodo


calc = Calculadora()
comodo = Comodo(input('Qual a profundidade do cômodo? '),
                input('Qual a largura do cômodo? ')
                )

print('A área das paredes é de ', calc.calcular_area_paredes(
    comodo.largura, comodo.profundidade, comodo.altura))

print('A área do teto é de ', calc.calcular_area_teto(
    comodo.largura, comodo.profundidade))

print('A litragem necessária é de ', calc.calcular_litragem_necessaria())
