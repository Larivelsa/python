from flask import render_template, url_for, redirect, request, send_from_directory
from app import app, db
from models import Categoria
from forms import CategoriaForm


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
    nome_categoria = request.form['nome_categoria']
    db.session.add(nova_categoria)
    db.session.commit()
    return redirect(url_for('listar_categoria'))

@app.route('/categorias/editar/<int:id>')
def editar_categoria_form(id):
    categoria = Categoria.query.filter_by(id=id).first()
    return render_template('editar_categoria_form.html', titulo='Editar Categoria', categorias=categorias)    

@app.route('/categorias/editar/<int:id>', methods=['POST'])
def atualizar_receita(id):
    receita = Receita.query.filter_by(id=id).first()
    receita.titulo = request.form['titulo']
    receita.id_categoria = request.form['categoria']
    receita.ingredientes = request.form['ingredientes']
    receita.preparo = request.form['preparo']
    db.session.commit()
    return redirect(url_for('listar_receita'))   

@app.route('/deletar_receita/<int:id>')
def deletar_receita(id):
    Receita.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('listar_receita'))        

'''
GET /categorias para listar

POST /categorias para criar

GET /categorias/<id> para visualizar uma categoria especifica

PUT /categorias/<id> para atualizar

DELETE /categorias/<id> para deletar
'''