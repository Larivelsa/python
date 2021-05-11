
try:
    arquivo = open('C:/Users/Larissa/github/python/manipulacao_arquivos/pessoas.csv')
    for registro in arquivo:
        print ('Nome: {} - Idade: {}'.format(*registro.split(',')))
finally:
    arquivo.close()


if arquivo.closed:
    print('Arquivo já foi fechado!')

