import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='banco_dados'
)

cursor = conexao.cursor()

sentenca_sql = 'DROP TABLE tabela_b'

# Usar o DROP TABLE IF EXISTS evitar gerar erro caso a tabela não existe mais
sentenca_sql_if_exists = 'DROP TABLE IF EXISTS tabela_b '
cursor.execute(sentenca_sql)
cursor.execute(sentenca_sql_if_exists)
conexao.close()
