'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido
'''
dia_semana = int(input('Informe um dia da semana (de 1 a 7): '))

if dia_semana == 1:
    dia_semana_por_extenso = 'Domingo'
elif dia_semana == 2:
    dia_semana_por_extenso = 'Segunda-feira'
elif dia_semana == 3:
    dia_semana_por_extenso = 'Terça-feira'
elif dia_semana == 4:
    dia_semana_por_extenso = 'Quarta-feira'
elif dia_semana == 5:
    dia_semana_por_extenso = 'Quinta-feira'
elif dia_semana == 6:
    dia_semana_por_extenso = 'Sexta-feira'
elif dia_semana == 7:
    dia_semana_por_extenso = 'Sábado'
else:
    dia_semana_por_extenso = 'Valor inválido'

print(f'Você quis dizer... {dia_semana_por_extenso}')