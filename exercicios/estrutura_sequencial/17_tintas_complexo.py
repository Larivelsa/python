'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- Comprar apenas latas de 18 litros;
- Comprar apenas galões de 3,6 litros;
- Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
  Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

'''

import math

area_pintada = float(input("Informe a quantidade de m² a ser pintada: "))
quantidade_litros = area_pintada / 6

if quantidade_litros < 18:
    latas_menores_apenas = quantidade_litros / 3.6
    print(f"Quantidade de litros: {quantidade_litros:.2f} e quantidade de latas de 3.6: {latas_menores_apenas}")
elif quantidade_litros % 18 == 0:
    latas_maiores_apenas = quantidade_litros / 18
    print(f"Quantidade de litros: {quantidade_litros:.2f} e quantidade de latas de 18: {latas_maiores_apenas}")
else:
    latas_maiores_mistas = quantidade_litros / 18
    decimal_latas_maiores_mistas = latas_maiores_mistas - int(latas_maiores_mistas)
    litros_para_dividir_nas_latas_menores = decimal_latas_maiores_mistas * 18
    latas_menores_mistas = litros_para_dividir_nas_latas_menores / 3.6
    print(f'''
              Quantidade de litros: {quantidade_litros:.2f}
              Latas de 3.6: {latas_menores_mistas}
              Latas de 18: {latas_maiores_mistas}
    ''')