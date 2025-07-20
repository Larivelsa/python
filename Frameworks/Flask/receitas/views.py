from flask import render_template, url_for, redirect, request, send_from_directory
from app import app, db
from models import Categoria, Receita

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/adicionar_categoria')
def adicionar_categoria():
    return render_template('adicionar_categoria.html',titulo='Adicionar categoria')

@app.route('/crud_criar_categoria', methods=['POST'])
def crud_criar_categoria():
    nome_categoria = request.form['nome_categoria']
       
    nova_categoria = Categoria(nome=nome_categoria)
    db.session.add(nova_categoria)
    db.session.commit()

    return redirect(url_for('inicio'))

@app.route('/listar_categoria')
def listar_categoria():
    categorias = Categoria.query.all()  # busca todas as categorias
    return render_template('listar_categoria.html', titulo='Categorias', categorias=categorias)

@app.route('/listar_receita')
def listar_receita():
    receitas = Receita.query.all()  # busca todas as categorias
    return render_template('listar_receita.html', titulo='Receitas', receitas=receitas)

@app.route('/receita/<int:id>')
def ver_receita(id):
    receita = Receita.query.get_or_404(id)
    return render_template('ver_receita.html', receita=receita)

@app.route('/adicionar_receita')
def adicionar_receita():
    categorias = Categoria.query.all()  # busca todas as categorias do banco
    return render_template('adicionar_receita.html', titulo='Adicionar receita', categorias=categorias)


@app.route('/crud_criar_receita', methods=['POST'])
def crud_criar_receita():
    titulo = request.form['titulo']
    id_categoria = request.form['categoria']
    ingredientes = request.form['ingredientes'] 
    preparo = request.form['preparo']
    
    nova_receita = Receita(titulo=titulo, id_categoria=id_categoria, ingredientes=ingredientes, preparo=preparo)
    db.session.add(nova_receita)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/deletar_receita/<int:id>')
def deletar_receita(id):
    Receita.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('listar_receita'))

@app.route('/editar_receita/<int:id>', methods=['GET'])
def editar_receita(id):
    receita = Receita.query.filter_by(id=id).first()
    categorias = Categoria.query.all()
    return render_template('editar_receita.html', receita=receita, titulo='Editar Receita', categorias=categorias)

@app.route('/atualizar_receita/<int:id>', methods=['POST',])
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