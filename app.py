
#imports do projeto
from flask import Flask
from flask import request, json, jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import render_template


app = Flask(__name__)



db = SQLAlchemy()
ma = Marshmallow(app)

mysql = MySQL(app)

#criaçao da classe do banco de dados
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


class Livros_Schema(ma.Schema):
    class Meta:
        fields = ("id", "titulo", "autor", "num_paginas", "custo")

livros_schema= Livros_Schema()
livros_schema = Livros_Schema(many=True)



app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/livraria"
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#criaçao do POST, com intuito de adicionar um objeto
@app.route('/livraria/add', methods=['POST'])
def adicionar_livro():
    
    titulo = request.json['titulo']
    autor = request.json['autor']
    num_paginas = request.json['num_paginas']
    custo = request.json['custo']

    if not (titulo and autor and num_paginas and custo):
        return jsonify({"message": "Campos obrigatórios faltando"}), 400

    novo_livro = Livraria(titulo=titulo, autor=autor, num_paginas=num_paginas, custo=custo)
    db.session.add(novo_livro)
    db.session.commit()

    return jsonify({"Message": "Seu livro foi adicionado com sucesso"})


#criaçao do GET, com intuito de listar os objetos
@app.route("/livraria", methods=['GET'])
def listar_livros():
    livraria = []
    data = Livraria.query.all()
    livraria = livros_schema.dump(data)
    return jsonify(livraria)


#criaçao do GET, com intuito de adicionar listar um objeto expecífico pelo id
@app.route("/livraria/<id>" , methods=['GET'] )
def livro_pelo_id(id):
    if str.isdigit(id) == False:
        return jsonify(f"Message: O id do livro não pode ser uma string")
    else:
        data = []
        livraria = Livraria.query.get(id)
        if livraria is None:
            return jsonify({"message": "Livro não encontrado"}), 404
        data.append(livraria)
        result = livros_schema.dump(data)
        return jsonify(result)


#criaçao do DELETE, com intuito de deletar um objeto
@app.route("/livraria/delete/<int:id>", methods=['DELETE'])
def excluir_livro(id):
    try:
        livraria = Livraria.query.get(id)
        if livraria is None:
            return jsonify({"message": "Livro não encontrado"}), 404

        db.session.delete(livraria)
        db.session.commit()

        return jsonify({"message": "Livro excluído com sucesso"})
    except Exception as e:
        return jsonify({"message": "Erro ao excluir o livro", "error": str(e)}), 500



#criaçao do PUT, com intuito de modificar/atualizar um objeto
@app.route("/livraria/atualizar/<int:id>", methods=['PUT'])
def atualizar_livro(id):
    try:
        livraria = Livraria.query.get(id)
        if livraria is None:
            return jsonify({"message": "Livro não encontrado"}), 404

        titulo = request.json.get('titulo', livraria.titulo)
        autor = request.json.get('autor', livraria.autor)
        num_paginas = request.json.get('num_paginas', livraria.num_paginas)
        custo = request.json.get('custo', livraria.custo)

        livraria.titulo = titulo
        livraria.autor = autor
        livraria.num_paginas = num_paginas
        livraria.custo = custo

        db.session.commit()

        return jsonify({"message": "Livro atualizado com sucesso"})
    except Exception as e:
        return jsonify({"message": "Erro ao atualizar o livro", "error": str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)