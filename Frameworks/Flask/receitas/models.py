from app import db

class Receita(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    ingredientes = db.Column(db.Text, nullable=False)
    preparo = db.Column(db.Text, nullable=False)

    categoria = db.relationship('Categoria', backref=db.backref('receitas', lazy=True))

    def __repr__(self):
        return f'<Receita {self.titulo}>'

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nome}>'
