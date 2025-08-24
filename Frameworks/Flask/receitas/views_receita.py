from flask import render_template, url_for, redirect, request, send_from_directory
from app import app, db
from models import Receita, Categoria

@app.route('/receitas/listar')
def listar_receita(): 
    receitas = Receita.query.all()  # busca todas as categorias
    return render_template('listar_receita.html', titulo='Receitas', receitas=receitas)

@app.route('/receita/<int:id>')
def ver_receita(id):
    receita = Receita.query.get_or_404(id)
    return render_template('ver_receita.html', receita=receita)

@app.route('/receitas/adicionar')
def adicionar_receita_form():
    categorias = Categoria.query.all()  # busca todas as categorias do banco
    return render_template('adicionar_receita.html', titulo='Adicionar receita', categorias=categorias)


@app.route('/receitas/adicionar', methods=['POST'])
def adicionar_receita():
    titulo = request.form['titulo']
    id_categoria = request.form['categoria']
    ingredientes = request.form['ingredientes'] 
    preparo = request.form['preparo']
    
    nova_receita = Receita(titulo=titulo, id_categoria=id_categoria, ingredientes=ingredientes, preparo=preparo)
    db.session.add(nova_receita)
    db.session.commit()
    return redirect(url_for('listar_receita'))

@app.route('/receitas/deletar/<int:id>')
def deletar_receita(id):
    Receita.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('listar_receita'))

@app.route('/receitas/editar/<int:id>')
def editar_receita_form(id):
    receita = Receita.query.filter_by(id=id).first()
    categorias = Categoria.query.all()
    return render_template('editar_receita_form.html', receita=receita, titulo='Editar Receita', categorias=categorias)

@app.route('/receitas/editar/<int:id>', methods=['POST'])
def atualizar_receita(id):
    receita = Receita.query.filter_by(id=id).first()
    receita.titulo = request.form['titulo']
    receita.id_categoria = request.form['categoria']
    receita.ingredientes = request.form['ingredientes']
    receita.preparo = request.form['preparo']
    
    db.session.commit()
    return redirect(url_for('listar_receita'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)