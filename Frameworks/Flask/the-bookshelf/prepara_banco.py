# criação do banco de dados e tabelas
import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306)


criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `the_bookshelf` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `the_bookshelf`;
    CREATE TABLE `leitura` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `data` DATE NOT NULL,
      `tipo` varchar(50) COLLATE utf8_bin NOT NULL,
      `formato` varchar(40) COLLATE utf8_bin NOT NULL,
      `titulo` varchar(40) COLLATE utf8_bin,
      `autor` varchar(40) COLLATE utf8_bin NOT NULL,
      `genero` varchar(40) COLLATE utf8_bin NOT NULL,
      `sinopse` varchar(768) COLLATE utf8_bin NOT NULL,
      `classificacao` INT(11) NOT NULL,      
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
   
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `nome` varchar(40) COLLATE utf8_bin NOT NULL,
      `senha` varchar(40) COLLATE utf8_bin,    
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;  
'''

cursor = conn.cursor()

cursor.execute(criar_tabelas)

cursor.executemany(
    'INSERT INTO leitura (data, tipo, formato, titulo, autor, genero, sinopse, classificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    [
        ('2020-01-01', 'livro', 'digital', 'Filosofia para Corajosos', 'Luis Felipe Ponde', 'filosofia',
         'O quao puramente politicamente correto o ser humano, de fato, pode ser tornar?', '4'),

        ('2020-12-05', 'livro', 'digital', 'O Ultimo Desejo', 'Andrzej Sapkowski', 'aventura',
         'Yennefer, aventuras incriveis e o bruxao mais sincerao: Geralt de Rivia.', '5')
    ])


cursor.execute('select * from leitura')
print(' -------------  Leituras:  -------------')
for leitura in cursor.fetchall():
    print(leitura[1])

conn.commit()
cursor.close()
