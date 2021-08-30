'''
instalar o flask na versão abaixo:
pip3 install flask==0.12.2
'''

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)  # __name__ obtem nome do módulo#
app.secret_key = 'chave_secreta'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Arcade', 'Nintendo')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'Nintendo')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista de Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    else:
        return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['post', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    # pega informação da query da url:
    proxima = request.args.get('proxima')
    # o nome do atributo dentro do formulário que recebe a variável
    # proxima que possui o valor obtido na query da url:
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['post', ])
def autentica():
    senha = request.form['senha']
    if senha == 'mestra':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/')
    else:
        flash('Não logado, tente novamente!')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect('/')


app.run(debug=True)
