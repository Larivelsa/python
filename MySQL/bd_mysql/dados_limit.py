from conexao_server_db import conectar

conexao = conectar()

cursor = conexao.cursor()

# SELECT LIMIT seleciona determinado número de linhas
sentenca_sql = 'SELECT * FROM tabela_a LIMIT 5'

cursor.execute(sentenca_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)

conexao.close()
