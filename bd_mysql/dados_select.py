from conexao_server_db import conectar

conexao = conectar()

cursor = conexao.cursor()
sentenca_sql = 'SELECT * FROM tabela_a'

cursor.execute(sentenca_sql)


# O método fetchmany() busca um número definido de linhas
# utilizando o parâmetro size
resultado_fetchmany = cursor.fetchmany(size=2)
for x_fetch_many in resultado_fetchmany:
    print(x_fetch_many)
print('=-=-=-=-=-=-=-=-=-=-=-=-=')

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

# O método fetchone() retorna apenas a primeira linha de resultado
resultado_fetchone = cursor.fetchone()
print(resultado_fetchone)
print('=-=-=-=-=-=-=-=-=-=-=-=-=')
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

# O método fetchall() busca todas as linhas de resultado da última sentença executada.
# Retorna uma lista de tuplas ou uma lista vazia.
resultado_fetchall = cursor.fetchall()
for x_fetch_all in resultado_fetchall:
    print(x_fetch_all)

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#

# Os métodos de busca removem da lista o conjunto buscado.
# Por exemplo, se numa primeira vez buscamos duas linhas, com o fetchmany() e, em seguida,
# usamos o fetchall(), o método retornará apenas as linhas restantes, não incluindo as que já foram
# buscadas pelo primeiro método utilizado (no caso, fetchmany()).

# A conexão com o banco de dados deve ser fechada após usar o método fetchall().
conexao.close()
