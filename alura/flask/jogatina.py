'''
instalar o flask na versão abaixo:
pip3 install flask==0.12.2
'''

from flask import Flask, render_template

app = Flask(__name__)  # __name__ obtem nome do módulo#


@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos')


app.run()
