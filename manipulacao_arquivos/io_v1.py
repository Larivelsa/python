﻿arquivo = open('C:/Users/Larissa/github/python/manipulacao_arquivos/pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {} - Idade: {}'.format(*registro.split(',')))