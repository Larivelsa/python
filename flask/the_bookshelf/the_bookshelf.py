from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from models import Leitura, Usuario
from dao import LeituraDao, UsuarioDao

app = Flask(__name__)
# http://devfuria.com.br/python/modulos-pacotes/
# http://devfuria.com.br/python/entenda-__name__-__main__/
app.secret_key = 'livros'


app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "the_bookshelf"
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
leitura_dao = LeituraDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def pagina_inicial():
    return redirect(url_for('inicio'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nome
            flash(f'Sucesso no login! Olá, {session["usuario_logado"]}')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Senha ou usuário incorreto! Tente novamente.')
            return redirect(url_for('login'))
    else:
        flash('Senha ou usuário incorreto! Tente novamente.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado.')
    return redirect(url_for('inicio'))


@app.route('/inicio')
def inicio():
    return render_template('inicial.html')


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastro de leitura')


@app.route('/inserir', methods=['POST', ])
def inserir():
    data = request.form['data']
    tipo = request.form['tipo']
    formato = request.form['formato']
    titulo = request.form['titulo']
    autor = request.form['autor']
    genero = request.form['genero']
    sinopse = request.form['sinopse']
    classificacao = request.form['classificacao']

    leitura = Leitura(data, tipo, formato, titulo, autor,
                      genero, sinopse, classificacao)
    leitura_inserida = leitura_dao.salvar(leitura)

    if leitura_inserida:
        flash('Leitura inserida com sucesso!')
    else:
        flash('Leitura não foi inserida.')
    return render_template('novo.html', titulo='Cadastro de leitura')


@app.route('/listar')
def listar():
    lista = leitura_dao.listar()
    return render_template('listar.html', leituras=lista, titulo='Lista de leituras')


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    leitura = leitura_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando leitura', leitura=leitura)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    id = request.form['id']
    data = request.form['data']
    tipo = request.form['tipo']
    formato = request.form['formato']
    titulo = request.form['titulo']
    autor = request.form['autor']
    genero = request.form['genero']
    sinopse = request.form['sinopse']
    classificacao = request.form['classificacao']

    leitura = Leitura(data, tipo, formato, titulo, autor,
                      genero, sinopse, classificacao, id)
    leitura_inserida = leitura_dao.salvar(leitura)

    if leitura_inserida:
        flash('Leitura atualizada com sucesso!')
    else:
        flash('Leitura não foi atualizada.')
    lista = leitura_dao.listar()
    return render_template('listar.html', leituras=lista, titulo='Lista de leituras')


app.run(debug=True)
