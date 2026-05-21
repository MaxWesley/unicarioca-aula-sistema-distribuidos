from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/pedido")
def pedido():
    resposta = requests.get("http://localhost:5001/usuario")
    usuario = resposta.json()

    return jsonify({
        "pedido": "Notebook",
        "usuario": usuario["usuario"]
    })

if __name__ == "__main__":
    app.run(port=5002)