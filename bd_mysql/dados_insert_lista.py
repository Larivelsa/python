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
sentenca_sql = 'INSERT INTO livro (id_livro, nome_livro, id_autor) VALUES (%s,%s,%s)'

valores = [(1, 'Sorrindo para vida', 10),
           (2, 'Dinheiro na mão', 9),
           (3, 'Como não empobrecer', 8),
           (4, 'Táticas para vencer vendavais', 7),
           (5, 'Ping Pong: um viés econômico', 6),
           (6, 'Pegue e pague: vida e sociedade', 5),
           (7, 'Em busca do tesouro roubado', 4),
           # para passar valor como null para o MySQL (campo vazio)
           (8, 'Detecte oportunidades e obtenha lucro', None),
           (9, 'Cresça e veja as vestes de Salomão', 1),
           (10, 'Em busca do vale dourado', 10)]

# O método executemany() possibilita que mais de uma linha com dados (apenas dados com linhas multiplas
# e não setenças em linhas múltiplas) seja inserido ao db.
# Para executar linha múltiplas de sentenças SQL, devemos usar o método execute() com o parâmetro multi=True,
# ficando assim, por exemplo: execute(sentencas_sql, multi=True)
# Em suma, multiplas linhas de dados, use executemany()
# e para multiplas linhas de sentenças, use o execute(sentencas_sql, multi=True).
# e mais uma observação: ao usar o execute(sentencas_sql, multi=True), não é recomendado pela própria documentação do MySQL
# usar parâmetros. Ou seja, usa-se comando e valores em uma única linha. E isso alvez não seja tão versátil, bom...
# Cada caso é um caso.

cursor.executemany(sentenca_sql, valores)

conexao.commit()

# Contando quantas linhas foram usadas na sentença SQL
print(cursor.rowcount, 'registro(s) inserido(s).')

# O cursor é fechado após a contagem das linhas afetadas, senão retornará -1
cursor.close()
