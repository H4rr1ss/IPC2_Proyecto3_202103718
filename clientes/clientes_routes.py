from flask import Blueprint, jsonify, request
import json
from cargaXML.clases import Instancia
from db.database import DB

cliente = Blueprint('cliente', __name__)

def __filtro(body):
    if not('objCliente' in body):
        return body

    objClientesJson = body['objCliente']
    ret = json.loads(objClientesJson)
    return ret

@cliente.route('/cliente/crearCliente', methods=['POST'])
def crearCliente():

    data = request.get_json()
    # ------CLIENTE------
    body = __filtro(data)

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

def __filtroInstancia(body):
    if not('objInstancia' in body):
        return body

    objInstanciaJSON = body['objInstancia']
    retorno = json.loads(objInstanciaJSON)
    return retorno

@cliente.route('/cliente/crearInstancia', methods=['POST'])
def crearInstancia():

    data = request.get_json()
    # -------------instancia--------------
    body = __filtroInstancia(data)

    try:
        # VALIDACIONES---
        if not('nitCliente' in body and 'id' in body and 'idConfig' in body and 'nombre' in body and 'fechaInicio' in body and 'estado' in body and 'fechaFinal' in body):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if not(DB.verificacionNIT(body.get('nitCliente'))):
            return {'msg': 'Cliente no existente'}, 400

        if DB.verificarInstanciaExistente(body.get('nitCliente'), body.get('id')):
            return {'msg': 'Instancia con esa id ya existe.'}, 400
        #----------------

        instancia = Instancia(body['id'], body['idConfig'], body['nombre'], body['fechaInicio'], body['estado'], body['fechaFinal'])
        DB.addInstanciaAcliente(body.get('nitCliente'), instancia)
        return {'msg': 'Instancia creada exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500

@cliente.route('/cliente/cancelarInstancia', methods=['POST'])
def cancelarInstancia():
    body = request.get_json()

    try:
        # VALIDACIONES---
        if not('nitCliente' in body and 'idInstancia' in body):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if not(DB.verificacionNIT(body['nitCliente'])):
            return {'msg': 'Cliente no existente'}, 400

        if not(DB.verificarInstanciaExistente(body['nitCliente'], body['idInstancia'])):
            return {'msg': 'Instancia no existente'}, 400

        fechaHora = DB.modificacionesCliente(body['nitCliente'], body['idInstancia'])
        if fechaHora is None:
            return {'msg': 'Esta instancia ya se encontraba cancelada'}, 400
        #-----------------

        DB.agregarConsumo(body['nitCliente'], body['idInstancia'], 'pendiente', fechaHora)

        return {'msg': 'Instancia cancelada exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500
