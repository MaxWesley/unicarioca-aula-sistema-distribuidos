from flask import Flask, jsonify

app = Flask(__name__)

usuarios = {
    1: "Ana",
    2: "Bruno"
}

@app.route("/usuario/<int:id_usuario>")
def usuario(id_usuario):
    return jsonify({
        "id": id_usuario,
        "nome": usuarios.get(id_usuario)
    })

if __name__ == "__main__":
    app.run(port=5001)