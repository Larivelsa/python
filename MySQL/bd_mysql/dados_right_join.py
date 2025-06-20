from conexao_server_db import conectar

conexao = conectar()

print(conexao._password)  # - um underscore representa que o atributo é privado
# um underscore é diferente de dois underscores (name mangling, em que a variável tem uma mudança de fato de nome...
# pesquisar mais sobre name mangling)
# - é possível acessar o atributo e imprimir, já que é um objeto! Legal...
cursor = conexao.cursor()
# SELECT: seleciona as colunas a serem listadas
# FROM: a partir de
# RIGHT JOIN: valores que dão match em ambas colunas e também todas as linhas da tabela que estiverem à direita do comando
# ON: onde o campo de determinada coluna é igual ao campo da outra coluna

sentenca_sql = '''SELECT livro.id_livro, livro.nome_livro, livro.id_autor, autor.nome_autor, autor.id_autor 
                  FROM autor 
                  RIGHT JOIN livro 
                  ON livro.id_autor = autor.id_autor'''

# Aqui no RIGHT JOIN importa se 'autor' ou 'livro' estejam após o FROM/INNER RIGHT,
# pois além de todos as combinações, as linhas da coluna do que estiver a direita
# também serão selecionados (no caso, é a tabela 'livro'). Ou seja, mesmo que livro
# não tenha relação com 'autor', todas as linhas também aparecerão no SELECT

cursor.execute(sentenca_sql)

resultado = cursor.fetchall()

for x in resultado:
    print(x)

# Exibindo o número de linhas encontradas (que dão match, ou seja, combinam)
print(len(resultado))
