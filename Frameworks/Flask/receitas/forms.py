from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length

class CategoriaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=1, max=40)])
    enviar = SubmitField('Adicionar categoria')

class ReceitaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(min=1, max=50)])
    ingredientes = StringField('Ingredientes', validators=[DataRequired(), Length(min=1, max=1000)])
    preparo = StringField('Modo de Preparo', validators=[DataRequired(), Length(min=1, max=1000)])
    categoria = StringField('Categoria', validators=[DataRequired()])
    imagem = FileField('Imagem', validators=[FileRequired()])
    enviar = SubmitField('Adicionar receita')
