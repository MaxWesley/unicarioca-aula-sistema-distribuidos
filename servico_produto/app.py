from flask import Flask, jsonify

app = Flask(__name__)

produtos = {
    10: {"id": 10, "nome": "Notebook", "preco": 3500.00},
    20: {"id": 20, "nome": "Mouse", "preco": 80.00},
    30: {"id": 30, "nome": "Teclado", "preco": 150.00}
}

@app.route("/v1/produtos")
def listar_produtos():
    return jsonify(list(produtos.values()))

@app.route("/v1/produtos/<int:id_produto>")
def buscar_produto_id(id_produto):
    produto = produtos.get(id_produto)

    if produto is None:
        return jsonify({"error": "Produto não encontrado"}), 404

    return jsonify(produto)

if __name__ == "__main__":
    app.run(port=5002)