from flask import render_template, url_for, redirect, request, send_from_directory
from app import app, db
from models import Categoria
from forms import CategoriaForm

'''
categoria
'''

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/categorias/nova')
def mostrar_form_categoria():
    return render_template('adicionar_categoria.html',titulo='Adicionar categoria')

@app.route('/categorias', methods=['POST'])
def salvar_categoria():
    nome_categoria = request.form['nome_categoria']
    
    nova_categoria = Categoria(nome=nome_categoria)
    db.session.add(nova_categoria)
    db.session.commit()

    return redirect(url_for('listar_categoria'))

@app.route('/listar_categoria')
def listar_categoria():
    categorias = Categoria.query.all()  # busca todas as categorias
    return render_template('listar_categoria.html', titulo='Categorias', categorias=categorias)


