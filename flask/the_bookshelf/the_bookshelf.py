from flask import Flask

app = Flask(__name__)


@app.route('/')
def oooooo():
    return 'saiy hello'


@app.route('/inicio')
def oooo():
    return 'bye h5ello'


app.run(debug=True)
