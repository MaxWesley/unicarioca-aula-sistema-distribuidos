from flask import Flask, jsonify
import requests

app = Flask(__name__)

URL_USUARIO = "http://localhost:5001"
URL_PRODUTO = "http://localhost:5002"

@app.route("/pedido")
def pedido():
    resposta = requests.get(f"{URL_USUARIO}/usuario")
    usuario = resposta.json()

    return jsonify({
        "pedido": "Notebook",
        "usuario": usuario["usuario"]
    })

@app.route("/v1/pedido/<int:id_usuario>/<int:id_produto>")
def gerar_pedido(id_usuario, id_produto):
    try:
        resposta_usuario = requests.get(
            f"{URL_USUARIO}/v2/usuarios/{id_usuario}",
            timeout=2
        )

        resposta_produto = requests.get(
            f"{URL_PRODUTO}/v1/produtos/{id_produto}",
            timeout=2
        )

        if resposta_usuario.status_code != 200:
            return jsonify({"error": "Não foi possível obter usuário"}), 502
        if resposta_produto.status_code != 200:
            return jsonify({"error": "Não foi possível obter produto"}), 502
        
        usuario = resposta_usuario.json()
        produto = resposta_produto.json()

        pedido = {
            "usuario": usuario["nome_completo"],
            "produto": produto["nome"],
            "preco": produto["preco"],
            "status": "pedido gerado"
        }

        return jsonify(pedido)
    except requests.exceptions.RequestException:
        return jsonify({
            "erro": "Falha de comunicação entre os serviços"
        }), 503
    
if __name__ == "__main__":
    app.run(port=5003)