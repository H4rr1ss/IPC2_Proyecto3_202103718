from flask import Blueprint, jsonify, request
import json
from db.database import DB

categoria = Blueprint('categoria', __name__)

def __filtro(body):
    if not ('objCategoria' in body):
        return body

    objCategoriaJson = body['objCategoria']
    retorno = json.loads(objCategoriaJson)
    return retorno

@categoria.route('/categoria/crearCategoria', methods=['POST'])
def crearCategoria():
    data = request.get_json()
    # -----CATEGORIAS-----
    body = __filtro(data)
    try:
        # VALIDACIONES---
        if not ('id' in body and 'nombre' in body and 'descripcion' in body and 'cargaTrabajo' in body and 'listaConfiguraciones' in body):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if DB.verificacionCategoriaID(body.get('id')):
            return {'msg': 'Categoria duplicada'}, 400
        # ---------------

        DB.addCategoria(body['id'], body['nombre'], body['descripcion'], body['cargaTrabajo'], body['listaConfiguraciones'])
        return {'msg': 'Categoria creada exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500

def __filtroConfig(body):
    if not ('objConfig' in body):
        return body

    objCategoriaJson = body['objConfig']
    retorno = json.loads(objCategoriaJson)
    return retorno

@categoria.route('/categoria/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    data = request.get_json()
    body = __filtroConfig(data)
    try:
        # VALIDACIONES---
        if not ('idCategoria' in body and 'id' in body and 'nombre' in body and 'descripcion' in body and 'listaRecursos'):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if not(DB.verificacionCategoriaExistente(body.get('idCategoria'))):
            return {'msg': 'Categoria no existente.'}, 400

        if DB.verificacionConfigID(body.get('idCategoria'), body.get('id')):
            return {'msg': 'Configuracion duplicada'}, 400
        # ---------------

        DB.addConfiguracion(body.get('idCategoria'), body['id'], body['nombre'], body['descripcion'], body['listaRecursos'])
        return {'msg': 'Configuración creada exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500
