from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
# http://devfuria.com.br/python/modulos-pacotes/
# http://devfuria.com.br/python/entenda-__name__-__main__/
app.secret_key = 'livros'


class Livro:
    def __init__(self, titulo, autor, genero, sinopse, nota, data):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.sinopse = sinopse
        self.nota = nota
        self.data = data


class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


usuario1 = Usuario('larissa91', 'Larissa', '1234')
usuario2 = Usuario('mateus96', 'Mateus', 'tibia')
usuario3 = Usuario('klaus21', 'Klaus', 'lulu')

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}

lista = []


@app.route('/')
def pagina_inicial():
    return redirect('/inicio')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', 'GET', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = request.form['usuario']
            flash('Sucesso no login!')
            proxima_pagina = request.form['proxima']
            return redirect(f'/{proxima_pagina}')
        else:
            flash('Senha ou usuário incorreto! Tente novamente.')
            return redirect('/login')
    else:
        flash('Senha ou usuário incorreto! Tente novamente.')
        return redirect('/login')


@app.route('/logout')
def deslogar():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado.')
    return redirect('/inicio')


@app.route('/inicio')
def barras():
    return render_template('inicial.html')


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Cadastro de livro')


@app.route('/inserir', methods=['POST', ])
def inserir():
    titulo = request.form['titulo']
    autor = request.form['autor']
    genero = request.form['genero']
    sinopse = request.form['sinopse']
    nota = request.form['nota']
    data = request.form['data']
    livro = Livro(titulo, autor, genero, sinopse, nota, data)
    lista.append(livro)

    if lista:
        flash('Leitura inserida com sucesso!')
    else:
        flash('Leitura não foi inserida.')
    return render_template('novo.html', titulo='Cadastro de leitura')


@app.route('/listar')
def listar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=listar')
    return render_template('listar.html', livros=lista, titulo='Lista de leituras')


app.run(debug=True)
