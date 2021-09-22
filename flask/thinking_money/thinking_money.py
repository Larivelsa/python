from flask import Flask

app = Flask(__name__)

# cria uma rota para server/inicio
# é necessário que haja uma função abaixo para gerar 
# o conteúdo da página
@app.route('/inicio')
def ola():
    return '<h2>Olá Flask!</h2>'

app.run(debug=True)

