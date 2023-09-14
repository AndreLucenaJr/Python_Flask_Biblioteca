from flask import Flask, make_response, jsonify, request
from database import livros


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/livros', methods=['GET'])
def listar_livros():
    return make_response(jsonify(
        message = 'Lista de todos os livros.', 
        data = livros))


# Rota para obter um livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        return jsonify(livro)
    return jsonify({"mensagem": "Livro não encontrado"}), 404



@app.route('/livros', methods=['POST'])
def adicionar_livro():
    livro = request.json
    livros.append(livro)
    return make_response(jsonify(
        message = 'livro cadrastado com sucesso', 
        livro = livro
    ))


# Rota para atualizar um livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro = next((livro for livro in livros if livro['id'] == id), None)
    if livro:
        dados_atualizados = request.get_json()
        livro['titulo'] = dados_atualizados.get('titulo', livro['titulo'])
        livro['autor'] = dados_atualizados.get('autor', livro['autor'])
        return jsonify(livro)
    return jsonify({"mensagem": "Livro não encontrado"}), 404



app.run()

