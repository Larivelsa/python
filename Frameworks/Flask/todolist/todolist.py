from flask import Flask, render_template, url_for, request, redirect, flash
import time, secrets

class Tarefa:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

lista=[]

app = Flask(__name__)
app.secret_key = 'klaus'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Lista de Tarefas', tarefas=lista)

@app.route('/nova')
def nova():
    return render_template('nova.html', titulo='Nova Tarefa')

@app.route('/criar', methods=['POST',])
def criar():
    descricao = request.form['descricao']
    id = f'{int(time.time())}{str(secrets.token_hex(3))}' # Gera um ID único com base no tempo e um token aleatório

    tarefa = Tarefa(id, descricao)
    lista.append(tarefa)
    return redirect(url_for('index'))

@app.route('/concluir/<id>')
def concluir(id):
    for tarefa in lista:
        if tarefa.id == id:
            lista.remove(tarefa)
    flash(f'Tarefa {tarefa.descricao} concluída!')
    if len(lista) == 0:
        flash('Todas as tarefas foram concluídas!')
    return redirect(url_for('index'))


app.run(debug=True)