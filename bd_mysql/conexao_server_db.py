# Módulo de conexão com banco de dados
import mysql.connector

def conectar():
    conexao = mysql.connector.connect(user='root',
                                      password='root',
                                      host='localhost',
                                      database='banco_dados')
                                      
    return conexao