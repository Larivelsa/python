import mysql.connector

def conectar():
    conexao = mysql.connector.connect(user='root',
                                      password='root',
                                      host='localhost')

# tipos de módulos em python: 
# https://docs.python.org/pt-br/3/tutorial/modules.html