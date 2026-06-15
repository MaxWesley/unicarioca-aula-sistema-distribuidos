from flask import Flask, jsonify, request

app = Flask(__name__)

banco = {}

@app.route("/replicar", methods=["POST"])
def replicar():
    pedido = request.get_json()
    banco[pedido["id"]] = pedido
    return jsonify({"status": "replicado", "pedido": pedido})

@app.route("/pedido/<id_pedido>")
def consultar(id_pedido):
    pedido = banco.get(id_pedido)
    
    if pedido is None:
        return jsonify({"erro": "Pedido nao encontrado no follower"}), 404
    
    return jsonify(pedido)

if __name__ == "__main__":
    app.run(port=5002)

