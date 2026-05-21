from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/usuario")
def usuario():
    return jsonify({"usuario": "Max"})

if __name__ == "__main__":
    app.run(port=5001)