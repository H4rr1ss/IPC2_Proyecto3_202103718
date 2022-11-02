from flask import Blueprint, jsonify, request
import json

from db.database import DB

cliente = Blueprint('cliente', __name__)


def filtro(body):
    if not('objCliente' in body):
        return body

    objClientesJson = body['objCliente']
    return objClientesJson


@cliente.route('/cliente/crearCliente', methods=['POST'])
def crearCliente():

    data = request.get_json()
    # ------CLIENTE------
    body = filtro(data)

    try:
        # VALIDACIONES---
        if not ('nit' in body and 'nombre' in body and 'usuario' in body and 'clave' in body and 'direccion' in body and 'correoElectronico' in body and 'listaInstancias'):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if DB.verificacionNIT(body.get('nit')):
            return {'msg': 'cliente duplicado'}, 400
        # ---------------

        DB.agregarCliente(body['nit'], body['nombre'], body['usuario'], body['clave'], body['direccion'], body['correoElectronico'], body['listaInstancias'])
        return {'msg': 'Cliente creado exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500

@cliente.route('/cliente/crearInstancia', methods=['POST'])
def crearInstancia():
    body = request.get_json()
    # -------------instancia--------------
    objInstanciaJson = body['objInstancia']
    objInstancia = json.loads(objInstanciaJson)
    print(objInstancia)
    return jsonify({'msg': 'ruta creacion de instancias'})


    