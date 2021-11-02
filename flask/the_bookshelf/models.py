class Leitura:
    def __init__(self, data, tipo, formato, titulo, autor, genero, sinopse, classificacao, id=None):
        self.data = data
        self.tipo = tipo
        self.formato = formato
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.sinopse = sinopse
        self.classificacao = classificacao
        self.id = id


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
