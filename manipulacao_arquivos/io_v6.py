import csv

with open('C:/Users/Larissa/github/python/manipulacao_arquivos/pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {} Idade: {}'.format(*pessoa))