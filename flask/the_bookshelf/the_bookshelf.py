from flask import Flask, render_template

app = Flask(__name__)
# http://devfuria.com.br/python/modulos-pacotes/
# http://devfuria.com.br/python/entenda-__name__-__main__/


@app.route('/inicial')
def barras():
    return render_template('inicial.html')


@app.route('/list')
def listar():
    lista = ('O Cavaleiro Preso na Armadura',
             'A Riqueza de uma Vida Simples', 'Os Segredos da Mente Milionária')
    return render_template('lista.html', livros=lista)


app.run(debug=True)
