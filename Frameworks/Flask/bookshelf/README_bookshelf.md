
# 📚 Catálogo de Livros

Aplicação web desenvolvida com **Python Flask** para cadastro e gerenciamento de um catálogo de livros. Ideal para leitores, bibliotecas pessoais ou sistemas educacionais.

## 🚀 Funcionalidades

- Cadastro de **livros** com:
  - Título
  - Autor
  - Ano de publicação
  - Gênero (ficção, técnico, biografia, etc.)
  - Avaliação pessoal (nota)
  - Upload de capa (opcional)
- Busca e filtro por título, autor ou gênero
- Visualização detalhada de cada livro
- Edição e exclusão de registros
- Interface limpa e responsiva

## 🧑‍💻 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [SQLite](https://www.sqlite.org/)
- [Jinja2](https://jinja.palletsprojects.com/)

## 🗂️ Estrutura de Diretórios

```
catalogo_livros/
├── app.py
├── models.py
├── forms.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── livro_detalhes.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
├── migrations/
└── README_bookshelf.md
```

## ⚙️ Instalação e Execução

1. Clone o repositório:
```bash
git clone https://github.com/seunome/catalogo-livros.git
cd catalogo-livros
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
flask run
```

Acesse em `http://127.0.0.1:5000`.

## 📈 Expansões Futuras

- Login de usuário para catalogar livros por perfil
- Comentários ou resenhas para cada livro
- Sistema de favoritos
- Exportação do catálogo em PDF ou CSV
- Consumo de API pública para preenchimento automático (ex: Google Books)

## 🧠 Aprendizados

Esse projeto permite praticar:
- CRUD completo com Flask
- Organização de templates e formulários
- Upload de imagens
- Busca e filtragem de dados
- Uso de ORM com SQLAlchemy

## 📄 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.
