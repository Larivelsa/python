from conexao_server import conectar

conexao = conectar()

# A classe cursor possibilita que o Python manipule sentenças SQL.
# Os cursores são criados pelo método connection.cursor() e isso faz
# com que os cursores fiquem vinculados à conexão e os comandos
# são executados no contexto da sessão de db envolvida na conexão.
cursor = conexao.cursor()

# Para ficar com o código mais legível, criei uma variável para
# receber a string com a setença SQL.
sql = 'CREATE DATABASE banco_dados'

# Passamos como argumento a sentença sql para o método .execute do objeto cursor
cursor.execute(sql)

# E pronto, o banco de dados foi criado via Python!

# E agora, fechamos a conexão após usar o cursor.
# Isso garante a redefinição de todo seu conteúdo e
# remoção de referências ao objeto criado anteriormente.
cursor.close()


# Não usamos o método commit() aqui porque não alteramos dado de tabela

'''
Este método envia uma COMMITinstrução ao servidor MySQL, confirmando a transação atual. 
Como, por padrão, o Conector / Python não se autocometa, é importante chamar esse método 
após cada transação que modifica dados para tabelas que usam mecanismos de armazenamento transacional.

'''
