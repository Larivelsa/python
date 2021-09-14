# instalar conector do mysql: python -m pip install mysql-connector-python

# importando API para lidar com o MySQL
import mysql.connector


# importante! Por segurança, não codifique os valores necessários para se conectar e fazer login no banco de dados em seu script principal.
# Python tem a convenção de um config.pymódulo, onde você pode manter esses valores separados do resto do seu código.
# fonte: https://dev.mysql.com/doc/connector-python/en/connector-python-coding.html

# cria um objeto de conexao com o mysql server, se definir o banco, conecta com o banco tb
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(conexao)

# cursor é uma estrutura de manipulação para executar as instruções DDL (Data Definition Language)
# o cursor está definido na classe CursorBase(MySQLCursorAbstract)
# cursor_teste recebe o objeto da conexao criada e aciona o método de cursor() da calsse e com isso conseguimos manipular a conexão
# cursor é do tipo iterável
cursor_teste = conexao.cursor()

# método execute() tb está definido na classe CursorBase(MySQLCursorAbstract) e retorna true se a operação foi executada
cursor_teste.execute("SHOW DATABASES")

for dbs in cursor_teste:
    print(dbs)
