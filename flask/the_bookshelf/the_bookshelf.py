from flask import Flask, render_template, request

app = Flask(__name__)
# http://devfuria.com.br/python/modulos-pacotes/
# http://devfuria.com.br/python/entenda-__name__-__main__/


class Livro:
    def __init__(self, titulo, autor, genero, sinopse, dataa):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.sinopse = sinopse
        self.data = dataa


lista = []


@app.route('/inicial')
def barras():
    return render_template('inicial.html')


@app.route('/novo')
def novo():
    return render_template('novo.html',titulo='Cadastro de livro')


@app.route('/inserir', methods=['POST', ])
def inserir():
    titulo = request.form['titulo']
    autor = request.form['autor']
    genero = request.form['genero']
    sinopse = request.form['sinopse']
    data = request.form['data']
    livro = Livro(titulo, autor, genero, sinopse, data)
    lista.append(livro)

    if lista:
        mensagem = 'Livro inserido com sucesso!'
    else:
        mensagem = 'O livro não foi inserido.'

    return render_template('novo.html', mensagem=mensagem, titulo='Cadastro de leitura')

@app.route('/listar')
def listar():
    return render_template('listar.html', livros=lista, titulo='Lista de leituras')


app.run(debug=True)
