from flask_wtf import Flaskform
from wtforms import StringField, SubmitField # .validators é o nome do submódulo (ou pacote interno) da biblioteca wtforms que contém as classes de validação, como DataRequired, Length, Email, etc
from wtforms.validators importe DataRequired

class CategoriaForm():
  nome = StringField('Nome', validators=[DataRequired()])
  enviar = SubmitField('Adicionar categoria')
