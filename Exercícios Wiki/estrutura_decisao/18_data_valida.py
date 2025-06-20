'''
Faça um Programa que peça uma data no formato dd/mm/aaaa 
e determine se a mesma é uma data válida. 
'''
data = input('Informe a data no formato dd/mm/aaaa: ')

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

mes_31 = [1, 3, 5, 7, 8, 10, 12]
mes_30 = [2, 4, 6, 9, 11]

valida_dia = False
valida_mes = False
valida_ano = False
print(mes)

if ano > 0:
    valida_ano = True
    if 0 < mes <= 12:
        valida_mes = True

        if mes in mes_31:
            if dia <= 31:
                valida_dia = True

        if mes in mes_30:
            if dia <= 30:
                valida_dia = True

validade = valida_dia and valida_mes and valida_ano

if validade:
    print(f'Data válida! Dia {dia}, mês {mes} e ano {ano}')
else:
    print(f'Data inválida! Dia {dia}, mês {mes} e ano {ano}')
