from flask import Flask, jsonify

from usuarios import usuarios
from produtos import produtos

from pedidos import gerar_pedido

app = Flask(__name__)

@app.route("/usuario/<int:id_usuario>")
def usuario(id_usuario):
    return jsonify({
        "id": id_usuario,
        "nome": usuarios.get(id_usuario),
    })

@app.route("/produto/<int:id_produto>")
def produto(id_produto):
    return jsonify(produtos.get(id_produto))


@app.route("/pedido/<int:id_usuario>/<int:id_produto>")
def pedido(id_usuario, id_produto):
    return jsonify(
        gerar_pedido(id_usuario, id_produto)
    )


if __name__ == "__main__":
    app.run(port=5000)