import flask
from flask import request, json, jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = flask.Flask(__name__)



db = SQLAlchemy()
ma = Marshmallow()

mysql = MySQL(app)


class Livraria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50),nullable=False)
    autor = db.Column(db.String(50),nullable =False)
    num_paginas = db.Column(db.Integer,nullable = False)
    custo = db.Column(db.Float,nullable = False)

    def __init__(self,titulo,autor,num_paginas,custo):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.custo = custo


class Livraria_livros(ma.Schema):
    class Meta:
        fields = ("id", "titulo", "autor", "num_paginas", "custo")

livraria_livros = Livraria_livros()
livraria_livros = Livraria_livros(many=True)



app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/livraria"
db.init_app(app)


with app.app_context():
    db.create_all()




@app.route('/livraria/add', methods=['POST'])
def adicionar_livro():
    _json = request.json
    titulo = _json['titulo']
    autor = _json['autor']
    num_paginas = _json['num_paginas']
    custo = _json['custo']
    novo_livro = Livraria(titulo=titulo, autor=autor, num_paginas=num_paginas, custo=custo)
    db.session.add(novo_livro)
    db.session.commit()

    return jsonify({"Message": "Seu livro foi adicionado com sucesso"})



@app.route("/livraria", methods=['GET'])
def listar_livros():
    livraria = []
    data = Livraria.query.all()
    livraria = livraria_livros.dump(data)
    return jsonify(livraria)



@app.route("/livraria/<id>" , methods=['GET'] )
def livro_pelo_id(id):
    data = []
    livraria = Livraria.query.get(id)
    data = livraria_livros.dump(livraria)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)