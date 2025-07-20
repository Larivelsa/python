import mysql.connector
from mysql.connector import errorcode


print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `receitas`;")

cursor.execute("CREATE DATABASE `receitas`;")

cursor.execute("USE `receitas`;")

# criando tabelas
TABLES = {}
TABLES['Categoria'] = ('''
      CREATE TABLE `categoria` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Receita'] = ('''
      CREATE TABLE `receita` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `id_categoria` int(11) NOT NULL,
      `titulo` varchar(50) NOT NULL,
      `ingredientes` varchar(500) NOT NULL,
      `preparo` varchar(500) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`id_categoria`) REFERENCES `categoria`(id) 
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
