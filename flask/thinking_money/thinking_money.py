from flask import Flask, render_template, url_for, request
# a classe Flask importada é para construção do aplicativo WSGI

# criando instância da classe e passando como parâmetro o nome do módulo onde o Flask vai procurar os recursos (modelos e arquivos estáticos)
app = Flask(__name__)


class Receita:
    def __init__(self, nome, tipo, data, valor):
        self.nome = nome
        self.tipo = tipo
        self.data = data
        self.valor = valor


# cria uma rota para server/inicio
# é necessário que haja uma função abaixo para gerar
# o conteúdo da página

# @app.route faz parte do Flask diz qual URL deve ser acionar a função
# e é decorator, sendo isso um padrão de projeto que adiciona
# uma nova funcionalidade a um objeto já existente
# fonte: https://www.datacamp.com/


@app.route('/inicio')
def ola():
    return f'<h2>Olá thinker money!</h2>'


@app.route('/receita')
def nova():
    return render_template('receita.html')


@app.route('/receita_criar', methods=['POST', ])
def receita_criar():
    nome = request.form['nome']
    tipo = request.form['tipo']
    data = request.form['data']
    valor = request.form['valor']

    receita = Receita(nome, tipo, data, valor)
    lista = lista.append(receita)

    return lista


@app.route('/e')
def e():
    return receita_criar().lista


# usa-se degub=True como parâmetro nomeado para que seja possível a visualização do log de
# acesso às páginas e também possibilitar o seu reinício em caso de alteração no código-fonte
# é usado apenas em ambiente de desenvolvimento, para produção usa-se a o deploy do WSGI
# e que não faz parte do objeto instanciado da classe
app.run(debug=True)

# próximo passo: ver templates
