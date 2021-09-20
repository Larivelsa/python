import mysql.connector

# Como vamos trabalhar especificamente com um db, vamos informar aqui no objeto da conexão
conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()

# Passando a sentença em string para uma variável a ser usada no método execute()
sql_livro = ('CREATE TABLE livro (id_livro INT, nome_livro VARCHAR(255), id_autor INT)')
cursor.execute(sql_livro)
sql_autor = ('CREATE TABLE autor (id_autor INT, nome_autor VARCHAR(255))')
cursor.execute(sql_autor)

# Criando a tabela

cursor.close()
