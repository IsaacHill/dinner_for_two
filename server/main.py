from flask import Flask, jsonify
from database import sqlite

app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home():
    return jsonify({
        'data': 'hello',
    })


@app.route("/db", methods=["POST"])
def db():
    """ Testing endpoint for DB creation"""
    sqlite.create_database()
    sqlite.create_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0")