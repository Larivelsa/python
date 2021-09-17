import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()
sentenca_sql = 'SELECT * FROM tabela_a WHERE campo_2 = (%s)'
# quanto acontece essa passagem de parâmetro do valor, o método execute() recebe uma lista (segundo parâmetro)
valor = ['18']

cursor.execute(sentenca_sql, valor)

resultado = cursor.fetchall()

for x in resultado:
    print(x)