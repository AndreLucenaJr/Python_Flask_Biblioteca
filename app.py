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
    livraria = livros_schema.dump(data)
    return jsonify(livraria)



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




@app.route('/livraria/add', methods=['GET'])
def formulario_adicionar_livro():
    return render_template('add_livro.html')




@app.route('/livraria/listar', methods=['GET'])
def listar_livros_page():
    data = Livraria.query.all()
    return render_template('listar_livros_page.html', livros=data)





if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)