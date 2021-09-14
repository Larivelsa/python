import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()

sql = 'INSERT INTO tabela_a (campo_1, campo_2) VALUES ("melancia",2)'

cursor.execute(sql)
# Fechamos aqui a conexão do cursor porque não usaremos mais, mas ainda a alteração não foi feita no banco de dados...
cursor.close()

# Agora sim, com o método commit(), as alterações que mandamos usando o método execute() do cursor afetarão a base de dados que estamos trabalhando.
conexao.commit()
