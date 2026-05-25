from flask import Flask, jsonify

app = Flask(__name__)

produtos = {
    10: {"nome": "Notebook", "preco": 3500},
    20: {"nome": "Mouse", "preco": 80}
}

@app.route("/produto/<int:id_produto>")
def produto(id_produto):
    return jsonify(produtos.get(id_produto))

if __name__ == "__main__":
    app.run(port=5002)