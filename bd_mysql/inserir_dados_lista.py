# Inserindo lista com tuplas de dados usando o método executemany()
import mysql.connector

conexao = mysql.connector.connect(user='root',
                                  password='root',
                                  host='localhost',
                                  database='banco_dados')

cursor = conexao.cursor()


# Aqui mudamos um pouco a forma de passar os valores, usamos os parâmetros posicionais (aí na sequência).
# Mesmo que estamos passando um valor inteiro, a sintaxe aqui do MySQL no Python aceita somente
# a marcação %s de String. Ou seja, testei com %d (para inteiros) e não rolou.
# Pode ser que eu aprenda algo novo, mas por enquanto vou usando o %s para os
# parâmetros sequenciais.


# O método executemany() possibilita que mais de uma linha com dados (apenas dados com linhas multiplas
# e não setenças em linhas múltiplas) seja inserido ao db.
# Para executar linha múltiplas de sentenças SQL, devemos usar o método execute() com o parâmetro multi=True,
# ficando assim, por exemplo: execute(sentencas_sql, multi=True)
# Em suma, multiplas linhas de dados, use executemany()
# e para multiplas linhas de sentenças, use o execute(sentencas_sql, multi=True).
# e mais uma observação: ao usar o execute(sentencas_sql, multi=True), não é recomendado pela própria documentação do MySQL
# usar parâmetros. Ou seja, usa-se comando e valores em uma única linha. E isso alvez não seja tão versátil, bom...
# Cada caso é um caso.



conexao.close() # fechar aqui a conexão não influencia em nada o atributos obtido do cursor

# Contando quantas linhas foram usadas na sentença SQL
print(cursor.rowcount, 'registro(s) inserido(s).')

# O cursor é fechado após a contagem das linhas afetadas, senão retornará -1
cursor.close()

sentenca_sql_ = 'INSERT INTO tabela_a (campo_1, campo_2) VALUES (%s,%s)'
valores_ = [('coisa', 20),
           ('geografia', 21)
]

cursor.executemany(sentenca_sql_, valores_)
conexao.commit()