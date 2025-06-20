'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320,
    310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
n = int(input('Informe um número inteiro positivo menor do que 1000: '))

if 0 <= n < 1000:
    n = str(n)
    tamanho = len(n)
    if tamanho == 1:
        mensagem = f'O número {n} possui 1 unidade, sendo o próprio número.'
    elif tamanho == 2:
        dezena = n[0]
        unidade = n[1]
        mensagem = f'O número {n} possui {dezena} dezena(s) e {unidade} unidade(s)'
    else:
        centena = n[0]
        dezena = n[1]
        unidade = n[2]
        mensagem = f'O número {n} possui {centena} centena(s) {dezena} dezena(s) e {unidade} unidade(s)'
else:
    print('Você não digitou um número maior que 0 e menor do que 1000! Tente novamente.')
    exit()

print(mensagem)
