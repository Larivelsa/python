from flask import Flask
# fazer pesquisa aqui: https://flask.palletsprojects.com/en/2.0.x/quickstart/

# __name__ é o nome do módulo
# por exemplo, se estiver trabalhando no script atual
# o __nam__ será main, mas se importamos um script
# chamado fibo no script main, o __name__
# será fibo
app = Flask(__name__)

# cria uma rota para server/inicio
# é necessário que haja uma função abaixo para gerar
# o conteúdo da página


@app.route('/inicio')
def ola():
    return '<h2>Olá Flask!</h2>'


app.run(debug=True)
