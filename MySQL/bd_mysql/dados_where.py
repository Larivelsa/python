from conexao_server_db import conectar

conexao = conectar()

cursor = conexao.cursor()

# SELECT com WHERE e LIKE
sentenca_sql = 'SELECT * FROM tabela_a WHERE campo_2 LIKE ("%%s%")'

# quanto acontece essa passagem de parâmetro do valor, o método execute() recebe uma lista (segundo parâmetro)
valor = [1]

cursor.execute(sentenca_sql, valor)

resultado = cursor.fetchall()

for x in resultado:
    print(x)
