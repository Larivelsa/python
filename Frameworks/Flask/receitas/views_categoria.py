from flask import render_template, url_for, redirect, request, send_from_directory
from app import app, db
from models import Categoria
from forms import CategoriaForm

@app.route('/categorias/nova')
def adicionar_categoria_form():
    return render_template('adicionar_categoria_form.html',titulo='Adicionar categoria')

@app.route('/categorias', methods=['POST'])
def salvar_categoria():
    nome_categoria = request.form['nome_categoria']
    nova_categoria = Categoria(nome=nome_categoria)
    db.session.add(nova_categoria)
    db.session.commit()
    return redirect(url_for('listar_categoria'))

@app.route('/categorias') # Por padrao, Flask assume GET, se usar POST, precisa declarar explicitamente
def listar_categoria():
    categorias = Categoria.query.all()
    return render_template('listar_categoria.html', titulo='Categorias', categorias=categorias)

'''
GET /categorias para listar

POST /categorias para criar

GET /categorias/<id> para visualizar uma categoria especifica

PUT /categorias/<id> para atualizar

DELETE /categorias/<id> para deletar
'''