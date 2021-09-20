import mysql.connector

conexao = mysql.connector.connect(
                                    host='localhost',
                                    user='root',
                                    password='root',
                                    database='banco_dados'
                                    )

print(conexao._password) # - um underscore representa que o atributo é privado
# um underscore é diferente de dois underscores (name mangling, em que a variável tem uma mudança de fato de nome...
# pesquisar mais sobre name mangling)
# - é possível acessar o atributo e imprimir, já que é um objeto! Legal...
cursor = conexao.cursor()
# SELECT: seleciona as colunas a serem listadas
# FROM: a partir de
# INNER JOIN: valores que dão match em ambas colunas
# ON: onde o campo de determinada coluna é igual ao campo da outra coluna

sentenca_sql = '''SELECT livro.id_livro, livro.nome_livro, livro.id_autor, autor.nome_autor, autor.id_autor 
                  FROM livro 
                  INNER JOIN autor 
                  ON livro.id_autor = autor.id_autor'''

cursor.execute(sentenca_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)
    
print(len(resultado))
