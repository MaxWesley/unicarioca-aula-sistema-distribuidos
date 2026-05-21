from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/usuario")
def usuario():
    return jsonify({"usuario": "Max"})

@app.route("/pedido")
def pedido():
    return jsonify({
        "pedido": "Notebook",
        "usuario": "Fabio"
    })

if __name__ == "__main__":
    app.run(port=5000)