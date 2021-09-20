# Primeiro, é necessário importar a API de comunicação entre o MySQL e Python
import mysql.connector

# Caso o driver da API não esteja instalado, fazer o download usando o pip:
# por exemplo, em C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python

# Agora vamos instanciar um objeto contendo as informações de conexão, usando a função connect,
# retornando um objeto MySQLConnection ou PooledMySQLConnection.
# Na função connect, passamos argumentos nomeados.
# Para conectar com server, passamos apenas user, password e host.
# Se necessário conectar ao db, informa database nos parâmetros.

# Exemplo de conexão com o server, sem expecificar a base de dados:
conexao_server = mysql.connector.connect(user='root',
                                        password='root',
                                        host='localhost')

# Exemplo de conexão com o server e também com um db:
conexao_server_e_bd = mysql.connector.connect(user='root',
                                              password='root',
                                              host='localhost',
                                              database='teste')

# Como a variável conexao recebeu uma instância do objeto,
# é possível acessar seus atributos (user,pw, host, por exemplo).
# Estes atributos estão 

                                              