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
    form = CategoriaForm(request.form)
    return render_template('adicionar_categoria_form.html',titulo='Adicionar categoria', form=form)

@app.route('/categorias/nova', methods=['POST'])
def adicionar_categoria():
    form = CategoriaForm(request.form)

    if not form.validate():
        return redirect(url_for('adicionar_categoria_form'))
 
    nome = form.nome.data
    nova_categoria = Categoria(nome=nome)
    db.session.add(nova_categoria)
    db.session.commit()
    return redirect(url_for('listar_categoria'))

@app.route('/categorias/editar/<int:id>')
def editar_categoria_form(id):
    categoria = Categoria.query.filter_by(id=id).first()
    form = CategoriaForm(request.form)    
    
    return render_template('editar_categoria_form.html', titulo='Editar Categoria', categoria=categoria, form=form)    

@app.route('/categorias/editar', methods=['POST'])
def editar_categoria(id):
    
    form = CategoriaForm(request.form)
    if form.validate_on_submit():
        categoria = Categoria.query.filter_by(id=id).first()
        categoria.nome = form.nome.data
        db.session.add(categoria) 
        db.session.commit()
        return redirect(url_for('listar_categoria'))   

@app.route('/categorias/deletar/<int:id>')
def deletar_categoria(id):
    Categoria.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('listar_categoria'))