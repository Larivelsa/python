import mysql.connector

db_teste = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="teste"
)

cursor_teste = db_teste.cursor()
# cursor_teste.execute("CREATE TABLE pessoas (nome VARCHAR(255), ano INT)")
instrucao_sql = "INSERT INTO pessoas (nome, ano) VALUES (%s, %s)"
valores = [("Ben", "1956"),
           ("Jay", "1953"),
           ("Georgia", "1989"),
           ("Bly", "1990"),
           ("Carla", "1945"),
           ("Verona", "1963"),
           ("Vivian", "1976")
           ]
# o método executemany() recebe a instrução e sequencia de parâmetros e prepara o banco para a transação
cursor_teste.executemany(instrucao_sql, valores)


# o método commit() sempre será necessário para confirmar as transações na tabela
# o mysql connector não se autocommita no python
db_teste.commit()
