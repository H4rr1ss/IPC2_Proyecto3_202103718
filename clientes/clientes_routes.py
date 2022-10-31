from flask import Blueprint, jsonify, request
import json

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente/crearCliente', methods=['POST'])
def crearCliente():
    body = request.get_json()
    # ------CLIENTE------
    objClientesJson = body['objCliente']
    objCliente = json.loads(objClientesJson)
    print(objCliente)
    return jsonify({'msg': 'ruta creacion de cliente'})

@cliente.route('/cliente/crearInstancia', methods=['POST'])
def crearInstancia():
    body = request.get_json()
    # -------------instancia--------------
    objInstanciaJson = body['objInstancia']
    objInstancia = json.loads(objInstanciaJson)
    print(objInstancia)
    return jsonify({'msg': 'ruta creacion de instancias'})