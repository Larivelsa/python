import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='banco_dados'
)

cursor = conexao.cursor()

# SELECT LIMIT seleciona determinado número de linhas
sentenca_sql = 'SELECT * FROM tabela_a LIMIT 5'

cursor.execute(sentenca_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)

conexao.close()
