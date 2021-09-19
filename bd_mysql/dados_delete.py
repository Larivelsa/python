import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()
sentenca_sql = 'DELETE FROM tabela_a WHERE campo_2 LIKE ("%%s")'
valores = [0]
cursor.execute(sentenca_sql, valores)
resultado = cursor.fetchall()

# Aqui precisa fazer o commit, pois houve alteração nos dados da tabela.
conexao.commit()

print(cursor.rowcount, 'linha(a) deletada(s).')
conexao.close()
