'''
instalar o flask na versão abaixo:
pip3 install flask==0.12.2
'''

from flask import Flask

app = Flask(__name__) #__name__ obtem nome do módulo#

@app.route('/inicio')
def ola():
    return '<h1>Hey you</h1>'

app.run()

