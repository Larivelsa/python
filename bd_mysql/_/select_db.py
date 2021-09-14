import mysql.connector

db_teste = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="teste"
)

cursor_teste = db_teste.cursor()

cursor_teste.execute("SELECT * FROM pessoas")
resultado1 = cursor_teste.fetchall()

cursor_teste.execute("SELECT * FROM pessoas where ano = 1956")
resultado2 = cursor_teste.fetchall()


for linhas in resultado1:
    print(linhas)

for linhas in resultado2:
    print(linhas)
