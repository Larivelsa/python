from flask_wtf import Flaskform
from wtforms import StringField, SubmitField # .validators é o nome do submódulo (ou pacote interno) da biblioteca wtforms que contém as classes de validação, como DataRequired, Length, Email, etc
from wtforms.validators importe DataRequired

class CategoriaForm(FlaskForm):
  nome = StringField('Nome', validators=[DataRequired(validators.Length(min=1, max=40)])])
  enviar = SubmitField('Adicionar categoria')

class ReceitaForm(FlaskForm):
  titulo = StringField('Título', validators=[DataRequired(min=1, max=50)])
  ingredientes = StringField('Ingredientes', validators=[DataRequired(validators.Length(min=1, max=1000)])]) 
  preparo = StringField('Modo de Preparo', validators=[DataRequired(validators.Length(min=1, max=1000)])]) 
  categoria = Stringfield('Categoria', validators=[DataRequired()])
  imagem = FileField(validators=[FileRequired()]) 
  enviar = SubmitField('Adicionar receita')
