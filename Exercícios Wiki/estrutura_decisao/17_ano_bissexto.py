'''
Faça um Programa que peça um número correspondente a um determinado ano e em 
seguida informe se este ano é ou não bissexto.
'''
ano = int(input('Informe um ano maior que zero: '))
if ano <= 0:
    print('Tás de brincas, informe um ano maior do que zero!')
    exit()

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Ano bissexto!')
        else:
            print('Não é um ano bissexto!')
    else:
        print('Ano bissexto!')
else:
    print('Não é ano bissexto!')


'''
1 - Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
2 - Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
3 - Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
4 - O ano é bissexto (tem 366 dias).
5 - O ano não é um ano bissexto (tem 365 dias).
'''
