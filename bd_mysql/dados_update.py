import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='banco_dados'
)

cursor = conexao.cursor()
# Sentença basicamente é assim, alterando o dado da tupla (linha): altere para novo_dado determinado campo de determinada coluna que possua determinado dado
sentenca_sql = 'UPDATE tabela_a SET campo_1 = "gato" WHERE campo_2 = "1"'
cursor.execute(sentenca_sql)

# Lembrar que é necessário o commit já que estamos alterando o dado de tabela
conexao.commit()
print(cursor.rowcount, 'linha(a) alterada(s).')
conexao.close()
