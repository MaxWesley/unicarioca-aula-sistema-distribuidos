from flask import Flask, jsonify
import requests
import time
import threading

app = Flask(__name__)

banco = {}
URL_FOLLOWER = "http://localhost:5002"

def replicar_com_atraso(pedido):
    time.sleep(5)
    
    try:
        requests.post(
            f"{URL_FOLLOWER}/replicar",
            json=pedido,
            timeout=2
        )
        print("Pedido replicado no follower")
    except:
        print("Falha ao replicar no follower")
        
@app.route("/criar/<id_pedido>/<float:valor>")
def criar(id_pedido, valor):
    
    if id_pedido in banco:
        return jsonify({
            "status": "Pedido já existia",
            "pedido": banco[id_pedido],
            "observacao": "Operacao idempotente"
        })
        
    pedido = {
        "id": id_pedido,
        "valor": valor,
        "status": "criado"
    }
    
    banco[id_pedido] = pedido
    
    threading.Thread(
        target=replicar_com_atraso,
        args=(pedido,)
    ).start()
    
    return jsonify({
        "status": "Gravado no leader",
        "pedido": pedido,
        "observacao": "Replicação ocorrera depois"
    })
    
@app.route("/pedido/<id_pedido>")
def consultar_leader(id_pedido):
    pedido = banco.get(id_pedido)
    
    if pedido is None:
        return jsonify({"error": "Pedido nao encontrado no leader"}), 404
    
    return jsonify(pedido)

@app.route("/reenviar/<id_pedido>")
def reenviar(id_pedido):
    pedido = banco.get(id_pedido)
    
    if pedido is None:
        return jsonify({"erro": "Pedido nao encontrado"}), 404
    
    try:
        requests.post(
            f"{URL_FOLLOWER}/replicar",
            json=pedido,
            timeout=2
        )
        return jsonify({"status": "Pedido reenviado ao follower"})
    except:
        return jsonify({"erro": "follower indisponível"}), 503
    
if __name__ == "__main__":
    app.run(port=5001)