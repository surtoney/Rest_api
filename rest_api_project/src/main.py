from flask import Flask, jsonify
from routes import *

app = Flask(__name__)


@app.route('/welkom')
def Welkom():
    return jsonify({"message": "Welcome to the REST API!"})


@app.route('/Tafel')
def Tafel():
    return jsonify({"message": "Hier is je Tafel!"})


if __name__ == '__main__':
    app.run(debug=True)
