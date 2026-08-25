from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios_db = []
_id_counter = 1

def gerar_id_unico():
    global _id_counter
    id_atual = _id_counter
    _id_counter += 1
    return id_atual

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios_db), 200

@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    dados = request.get_json()
    if not dados or not dados.get('nome') or not dados.get('email'):
        return jsonify({"error": "Falha na validação"}), 400
        
    novo_usuario = {
        "id": gerar_id_unico(),
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "perfil": dados.get("perfil", "usuario_padrao")
    }
    usuarios_db.append(novo_usuario)
    return jsonify({"data": novo_usuario}), 201

@app.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    for usuario in usuarios_db:
        if usuario.get('id') == id:
            return jsonify(usuario), 200
    return jsonify({"erro": "Not Found", "mensagem": "Não encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
