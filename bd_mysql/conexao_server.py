import mysql.connector

def conectar():
    conexao = mysql.connector.connect(user='root',
                                      password='root',
                                      host='localhost')
