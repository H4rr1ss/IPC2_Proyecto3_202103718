from flask import Blueprint, jsonify, request
import json
from cargaXML.clases import Instancia
from db.database import DB

cliente = Blueprint('cliente', __name__)

def filtro(body):
    if not('objCliente' in body):
        return body
    elif not('objInstancia' in body):
        return body

    objClientesJson = body['objCliente']
    ret = json.loads(objClientesJson)
    return ret

@cliente.route('/cliente/crearCliente', methods=['POST'])
def crearCliente():

    data = request.get_json()
    # ------CLIENTE------
    body = filtro(data)

    try:
        # VALIDACIONES---
        if not ('nit' in body and 'nombre' in body and 'usuario' in body and 'clave' in body and 'direccion' in body and 'correoElectronico' in body and 'listaInstancias' in body):
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

    data = request.get_json()
    # -------------instancia--------------
    body = filtro(data)

    try:
        # VALIDACIONES---
        if not('nitCliente' in body and 'id' in body and 'idConfig' in body and 'nombre' in body and 'fechaInicio' in body and 'estado' in body and 'fechaFinal' in body):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if DB.verificarClienteExistente(body.get('nitCliente')):
            return {'msg': 'Cliente no existente'}, 400

        if DB.verificarInstanciaExistente(body.get('nitCliente'), body.get('id')):
            return {'msg': 'Instancia con esa id ya existe.'}, 400
        #----------------

        instancia = Instancia(body['id'], body['idConfig'], body['nombre'], body['fechaInicio'], body['estado'], body['fechaFinal'])
        DB.addInstanciaAcliente(body.get('nitCliente'), instancia)
        return {'msg': 'Instancia creada exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500