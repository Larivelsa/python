from flask import render_template, url_for, redirect, request, send_from_directory
from app import app, db
from models import Categoria
from forms import AdicionarCategoriaForm

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/categorias') # Por padrao, Flask assume GET, se usar POST, precisa declarar explicitamente
def listar_categoria():
    categorias = Categoria.query.all()
    return render_template('listar_categoria.html', titulo='Categorias', categorias=categorias)    

@app.route('/categorias/nova')
def adicionar_categoria_form():
    return render_template('adicionar_categoria_form.html',titulo='Adicionar categoria')

@app.route('/categorias/nova', methods=['POST'])
def adicionar_categoria():
    nome = request.form['nome']
    nova_categoria = Categoria(nome=nome)
    db.session.add(nova_categoria)
    db.session.commit()
    return redirect(url_for('listar_categoria'))

@app.route('/categorias/editar/<int:id>')
def editar_categoria_form(id):
    categoria = Categoria.query.filter_by(id=id).first()
    return render_template('editar_categoria_form.html', titulo='Editar Categoria', categoria=categoria)    

@app.route('/categorias/editar/<int:id>', methods=['POST'])
def editar_categoria(id):
    categoria = Categoria.query.filter_by(id=id).first()
    categoria.nome = request.form['nome']

    editar_categoria = CategoriaForm(request.form)
    db.session.commit()
    return redirect(url_for('listar_categoria'))   

@app.route('/categorias/deletar/<int:id>')
def deletar_categoria(id):
    Categoria.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('listar_categoria'))