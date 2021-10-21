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

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/inserir')
def inserir():
    l1 = Livro('Os Segredos da Mente Milionária','T. Harv Eker','Finanças','Possuir mindset de riqueza é essencial.')
    lista.append(l1)
    return render_template('listar.html', livros=lista)

@app.route('/listar')
def listar():
    return render_template('listar.html',livros=lista)

app.run(debug=True) 