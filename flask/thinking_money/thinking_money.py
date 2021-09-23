from flask import Flask
# a classe Flask importada é para construção do aplicativo WSGI

# criando instância da classe e passando como parâmetro o nome do módulo onde o Flask vai procurar os recursos (modelos e arquivos estáticos)
app = Flask(__name__)

# cria uma rota para server/inicio
# é necessário que haja uma função abaixo para gerar
# o conteúdo da página

# @app.route faz parte do Flask e é um decorator e# um decorator é um método
# que envolve uma função e modifica seu comportamento (ainda não entendi completamente...)
# e diz qual URL deve ser acionar a função


@app.route('/inicio')
def ola():
    return '<h2>Olá Flask!</h2>'


# usa-se degub=True como parâmetro nomeado para que seja possível a visualização do log de
# acesso às páginas e também possibilitar o seu reinício em caso de alteração no código-fonte
app.run(debug=True)
