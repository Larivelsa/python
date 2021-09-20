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
sentenca_sql = 'INSERT INTO autor (id_autor, nome_autor) VALUES (%s,%s)'
                
valores = [(1,'Sócrates Alcântara'),
           (2,'Platão das Neves'),
           (3,'Mário Leitão'),
           (4,'Márcia Tibia'),
           (5,'Selena de Luminera'),
           (6,'Plínio Paulo'),
           (7,'Antônia Albuquerque'),
           (8,'Bill Jobs'),
           (9,'Steve Gates'),
           (10,'Elon Bezos')]

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