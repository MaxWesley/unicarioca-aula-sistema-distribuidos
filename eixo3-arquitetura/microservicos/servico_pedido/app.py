from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL_USUARIO = "http://localhost:5001"
URL_PRODUTO = "http://localhost:5002"

@app.route("/pedido/<int:id_usuario>/<int:id_produto>")
def pedido(id_usuario, id_produto):
    usuario = requests.get(f"{URL_USUARIO}/usuario/{id_usuario}").json()
    produto = requests.get(f"{URL_PRODUTO}/produto/{id_produto}").json()

    return jsonify({
        "usuario": usuario["nome"],
        "produto": produto["nome"],
        "preco": produto["preco"],
        "status": "pedido criado"
    })

if __name__ == "__main__":
    app.run(port=5003)