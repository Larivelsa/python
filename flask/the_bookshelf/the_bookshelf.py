from flask import Flask

app = Flask(__name__)
# http://devfuria.com.br/python/modulos-pacotes/
# http://devfuria.com.br/python/entenda-__name__-__main__/

@app.route('/')
def barra():
    return '<h1>É barra</h1>'

app.run(debug=True)