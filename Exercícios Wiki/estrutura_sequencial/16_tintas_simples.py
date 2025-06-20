'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
'''

import math

area_pintada = float(input("Informe a quantidade de m² a ser pintada: "))
quantidade_litros = area_pintada / 3
quantidade_latas = quantidade_litros / 18
quantidade_latas_arredondado_para_cima = math.ceil(quantidade_latas)
valor = quantidade_latas_arredondado_para_cima * 80

print(f'''
Quantidade de litros: {quantidade_litros:.2f}
Quantidade de latas: {quantidade_latas_arredondado_para_cima}
Valor gasto em latas de tinta: {valor:.2f}''')
