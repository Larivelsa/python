from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AdicionarCategoriaForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=2, max=40)])
    submit = SubmitField("Adicionar Categoria")
