from flask import Flask, render_template

app = Flask(__name__)
# http://devfuria.com.br/python/modulos-pacotes/
# http://devfuria.com.br/python/entenda-__name__-__main__/


class Livro:
    def __init__(self,titulo, autor, genero, sinopse):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.sinopse = sinopse

lista = []

@app.route('/inicial')
def barras():
    return render_template('inicial.html')


@app.route('/cria')
def criar():
    l2 = Livro('Os Segredos da Mente Milionária','T. Harv Eker','Finanças','Muito bom')
    lista.append(l2)
    return render_template('lista.html', livros=lista)

app.run(debug=True)
