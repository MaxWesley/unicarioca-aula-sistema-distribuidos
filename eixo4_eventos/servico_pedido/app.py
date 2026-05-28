from flask import Flask, jsonify
import json
app = Flask(__name__)

ARQUIVO_FILA = "fila.txt"

@app.route("/pedidos/<int:id_pedido>")
def criar_pedido(id_pedido):

    evento = {
        "tipo": "pedido_criado",
        "pedido_id": id_pedido,
        "cliente": "Ana",
        "valor": 3500
    }

    with open(ARQUIVO_FILA, "a") as fila:
        fila.write(json.dumps(evento) + "\n")

        return jsonify({
            "status": "evento enviado para fila",
            "pedido_id": id_pedido
        })
    
if __name__ == "__main__":
    app.run(port=5001)