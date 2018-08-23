from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home():
    return jsonify({
        'data': 'hello',
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0")