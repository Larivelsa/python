from flask_wtf import Flaskform
from wtforms import StringField, SubmitField # .validators é o nome do submódulo (ou pacote interno) da biblioteca wtforms que contém as classes de validação, como DataRequired, Length, Email, etc
from wtforms.validators importe DataRequired

class CategoriaForm(FlaskForm):
  nome = StringField('Nome', validators=[DataRequired(validators.Length(min=1, max=40)])])
  enviar = SubmitField('Adicionar categoria')

class ReceitaForm(FlaskForm):
  titulo = StringField('Título', validators=[DataRequired()])
  ingredientes = StringField('Ingredientes', validators=[DataRequired(validators.Length(min=1, max=50)])]) 
  preparo = StringField('Modo de Preparo', validators=[DataRequired(validators.Length(min=1, max=1000)])]) 
  preparo = StringField('Modo de Preparo', validators=[DataRequired(validators.Length(min=1, max=1000)])]) 

```
ver como validação de select field se necessário e o upload no wtforms
<div class="input-field col s12">
    <select name="categoria" id="categoria">
      <option value="" disabled selected>Escolha uma categoria</option>
      {% for categoria in categorias %}
      <option value="{{ categoria.id }}">{{ categoria.nome }}</option>
      {% endfor %}
    </select>
    <label for="categoria">Categoria</label>
  </div>

  <div class="input-field col s12">
    <figure class="col s1">
      <img class="responsive-img" src="{{ url_for('imagem', nome_arquivo='capa_padrao.png') }}" alt="Imagem de receitas" id="imagem-preview">
      <figcaption>
        <label class="fileContainer">
          <input type="file" name="arquivo" accept=".jpg,.png">
        </label>
      </figcaption>
    </figure>
  </div>

  <button class="btn waves-effect waves-light" type="submit">Adicionar receita</button>
  <a class="btn waves-effect waves-light" href="{{ url_for('inicio') }}">Início</a>
</form>
  ```
