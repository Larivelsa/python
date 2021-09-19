import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()

sentenca_sql = 'SELECT * FROM tabela_a WHERE campo_2 LIKE ("%%s%") ORDER BY campo_1 DESC'
valores = [1]

cursor.execute(sentenca_sql, valores)
resultado = cursor.fetchall()

for x in resultado:
    print(x)
