from flask import Flask, jsonify
from flask_cors import CORS
from client.client_routes import client

app = Flask(__name__)
CORS(app)

prueba = {'msg': 'Esta es una api works!!'}

@app.route('/prueba', methods=["GET"])
def index():
    return jsonify(prueba)

app.register_blueprint(client)