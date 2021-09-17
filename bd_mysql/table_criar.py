import mysql.connector

# Como vamos trabalhar especificamente com um db, vamos informar aqui no objeto da conexão
conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()

# Passando a sentença em string para uma variável a ser usada no método execute()
sql = ('CREATE TABLE tabela_a (campo_1 VARCHAR(255), campo_2 INT)')

# Criando a tabela
cursor.execute(sql)

cursor.close()
