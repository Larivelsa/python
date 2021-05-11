import csv

with open('C:/Users/Larissa/github/python/manipulacao_arquivos/desafio-ibge.csv') as arquivo:
    with open('C:/Users/Larissa/github/python/manipulacao_arquivos/desafio-ibge.txt','w') as saida:
        for linha in csv.reader(arquivo):
            print('Quarto: {8} - Oitavo: {3}'.format(*linha),file=saida)