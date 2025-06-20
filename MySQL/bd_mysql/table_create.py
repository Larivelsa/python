from conexao_server_db import conectar

conexao = conectar()

cursor = conexao.cursor()

# Passando a sentença em string para uma variável a ser usada no método execute()
sql_livro = ('CREATE TABLE livro (id_livro INT, nome_livro VARCHAR(255), id_autor INT)')
cursor.execute(sql_livro)
sql_autor = ('CREATE TABLE autor (id_autor INT, nome_autor VARCHAR(255))')
cursor.execute(sql_autor)

cursor.close()
