import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()
sentenca_sql = 'SELECT * FROM tabela_b'

cursor.execute(sentenca_sql)

# O método fetchall() busca todas as linhas de resultado da última sentença executada.
# Retorna uma lista de tuplas ou uma lista vazia.
resultado = cursor.fetchall()

# Acredito que não há uma necessidade grande de ficar fechando cursos já que
# estamos fechando a conexão logo em seguida. Talvez seja interessante
# fechar o cursor quando temos mais de um...

for x in resultado:
    print(x)



# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#


# O método fetchone() retorna apenas a primeira linha de resultado
# verificar pq não retorna
resultado = cursor.fetchone()
print(resultado)



# A conexão com o banco de dados deve ser fechada após usar o método fetchall().
conexao.close()