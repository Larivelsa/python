
with open('C:/Users/Larissa/github/python/manipulacao_arquivos/pessoas.csv') as arquivo: # garante o fechamento
    for registro in arquivo:
        print ('Nome: {} - Idade: {}'.format(*registro.split(',')))

    arquivo.close()


if arquivo.closed:
    print('Arquivo já foi fechado!')

