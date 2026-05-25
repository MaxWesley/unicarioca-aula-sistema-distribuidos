from flask import Flask, jsonify

app = Flask(__name__)

usuarios = {
    1: "Ana",
    2: "Bruno"
}

produtos = {
    10: {"nome": "Notebook", "preco": 3500},
    20: {"nome": "Mouse", "preco": 80}
}

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
    usuario = usuarios.get(id_usuario)
    produto = produtos.get(id_produto)

    return jsonify({
        "usuario": usuario,
        "produto": produto["nome"],
        "preco": produto["preco"],
        "status": "pedido gerado"
    })

if __name__ == "__main__":
    app.run(port=5000)