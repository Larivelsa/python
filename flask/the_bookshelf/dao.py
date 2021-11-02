# abstração do banco de dados
from models import Leitura, Usuario

SQL_DELETA_LEITURA = 'DELETE FROM leitura WHERE id = %s'
SQL_LEITURA_POR_ID = 'SELECT id, data, tipo, formato, titulo, autor, genero, sinopse, classificacao FROM leitura WHERE id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha FROM user WHERE id = %s'
SQL_ATUALIZA_LEITURA = 'UPDATE leitura SET data=%s, tipo=%s, formato=%s, titulo=%s, autor=%s, genero=%s, sinopse=%s, classificacao=%s WHERE id = %s'
SQL_BUSCA_LEITURAS = 'SELECT id, data, tipo, formato, titulo, autor, genero, sinopse, classificacao FROM leitura'
SQL_CRIA_LEITURA = 'INSERT into leitura (data, tipo, formato, titulo, autor, genero, sinopse, classificacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'


class LeituraDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, leitura):
        cursor = self.__db.connection.cursor()

        if (leitura.id):
            cursor.execute(SQL_ATUALIZA_LEITURA, (leitura.data, leitura.tipo, leitura.formato,
                           leitura.titulo, leitura.autor, leitura.genero, leitura.sinopse, leitura.classificacao, leitura.id))
        else:
            cursor.execute(SQL_CRIA_LEITURA, (leitura.data, leitura.tipo, leitura.formato,
                           leitura.titulo, leitura.autor, leitura.genero, leitura.sinopse, leitura.classificacao))
            leitura.id = cursor.lastrowid
        self.__db.connection.commit()
        return leitura

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LEITURAS)
        leituras = traduz_leituras(cursor.fetchall())
        return leituras

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LEITURA_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Leitura(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_LEITURA, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_leituras(leituras):
    def cria_leitura_com_tupla(tupla):
        return Leitura(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], id=tupla[0])
    return list(map(cria_leitura_com_tupla, leituras))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
