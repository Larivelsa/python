
with open('C:/Users/Larissa/github/python/manipulacao_arquivos/pessoas.csv') as arquivo: # garante o fechamento
    with open('C:/Users/Larissa/github/python/manipulacao_arquivos/pessoas.txt','w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print ('Nome: {} - Idade: {}'.format(*pessoa),file=saida)

if arquivo.closed:
    print('Arquivo já foi fechado!')

if saida.closed:
    print('Arquivo de saída já foi fechado!')

