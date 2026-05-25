from flask import Flask
import requests

app = Flask(__name__)

URL_PEDIDO = "http://localhost:5003"

@app.route("/gateway/pedido/<int:id_usuario>/<int:id_produto>")
def gateway(id_usuario, id_produto):
    resposta = requests.get(
        f"{URL_PEDIDO}/pedido/{id_usuario}/{id_produto}"
    )

    return resposta.json()

if __name__ == "__main__":
    app.run(port=5000)