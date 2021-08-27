'''
instalar o flask na versão abaixo:
pip3 install flask==0.12.2
'''

from flask import Flask, render_template

app = Flask(__name__)  # __name__ obtem nome do módulo#

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')

def ola():
    jogo1 = Jogo('Super Mario','Arcade','Nintendo')
    jogo2 = Jogo('Pokemon Gold','RPG','GBA')
    jogo3 = Jogo('Mortal Kombat','Luta','Nintendo')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
