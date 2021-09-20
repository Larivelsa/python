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



