# 📚 Coleção de Receitas

Projeto web para cadastrar, listar, editar e excluir receitas culinárias. Idealizado como uma aplicação simples para exercitar conhecimentos de desenvolvimento web com Flask e persistência de dados com SQLAlchemy.

## 🚀 Funcionalidades

- ✅ Cadastro de novas receitas  
- ✅ Edição de receitas existentes  
- ✅ Exclusão de receitas  
- ✅ Listagem de receitas com título, ingredientes e modo de preparo  
- ✅ Upload de imagem opcional para cada receita  

## 🛠️ Tecnologias utilizadas

- Python 3.x  
- Flask  
- SQLAlchemy  
- SQLite (pode ser facilmente substituído por outro banco)  
- HTML5 + CSS3  
- Bootstrap (ou outro framework CSS)  

## 🧱 Estrutura de diretórios (exemplo)

```
/colecao_receitas/
├── app.py
├── models.py
├── templates/
│   ├── index.html
│   ├── nova_receita.html
│   └── editar_receita.html
├── static/
│   └── imagens/
├── instance/
│   └── receitas.sqlite
├── README.md
└── requirements.txt
```

## ⚙️ Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/colecao-receitas.git
   cd colecao-receitas
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   flask run
   ```

5. Acesse em: `http://127.0.0.1:5000/`

## 💡 Possíveis melhorias

- Filtro de receitas por ingredientes ou categorias  
- Comentários de usuários  
- Integração com API externa de receitas  
- Responsividade avançada com CSS ou frameworks modernos  

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
