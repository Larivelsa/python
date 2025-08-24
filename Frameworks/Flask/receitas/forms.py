from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CategoriaForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=2, max=40)])
    salvar = SubmitField("Adicionar Categoria")
