from flask import Flask, jsonify

app = Flask(__name__)

usuarios = {
    1: {"id": 1, "nome": "Max"},
    2: {"id": 2, "nome": "Bruno"},
    3: {"id": 3, "nome": "Carla"},
}

@app.route("/v1/usuarios/<int:id_usuario>")
def buscar_usuario(id_usuario):
    usuario = usuarios.get(id_usuario)

    if usuario is None:
        return jsonify({"error": "Usuário não encontrado"}), 404

    return jsonify(usuario)



@app.route("/v1/usuarios")
def listar_usuarios():
    return jsonify(list(usuarios.values()))

if __name__ == "__main__":
    app.run(port=5001)