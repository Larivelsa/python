from flask import Flask, render_template, url_for, request
# a classe Flask importada é para construção do aplicativo WSGI

# criando instância da classe e passando como parâmetro o nome do módulo onde o Flask vai procurar os recursos (modelos e arquivos estáticos)
app = Flask(__name__)


class EventoFinanceiro:
    def __init__(self, nome, valor, data):
        self.nome = nome
        self.valor = valor
        self.data = data

class Receita(EventoFinanceiro):
    def __init__(self):
        pass





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



# usa-se degub=True como parâmetro nomeado para que seja possível a visualização do log de
# acesso às páginas e também possibilitar o seu reinício em caso de alteração no código-fonte
# é usado apenas em ambiente de desenvolvimento, para produção usa-se a o deploy do WSGI
# e que não faz parte do objeto instanciado da classe
app.run(debug=True)
