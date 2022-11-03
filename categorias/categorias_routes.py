from flask import Blueprint, jsonify, request
import json
from cargaXML.clases import Configuracion
from db.database import DB

categoria = Blueprint('categoria', __name__)


def filtro(body):
    if not ('objCategoria' in body):
        return body

    objCategoriaJson = body['objCategoria']
    ret = json.loads(objCategoriaJson)
    return ret


@categoria.route('/categoria/crearCategoria', methods=['POST'])
def crearCategoria():
    data = request.get_json()
    body = filtro(data)
    # -----CATEGORIAS-----
    try:
        # VALIDACIONES---
        if not ('id' in body and 'nombre' in body and 'descripcion' in body and 'cargaTrabajo' in body and 'listaConfiguraciones'):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if DB.verificacionID(body.get('id')):
            return {'msg': 'Categoria duplicada'}, 400
        # ---------------

        DB.addCategoria(body['id'], body['nombre'], body['descripcion'], body['cargaTrabajo'],
                        body['listaConfiguraciones'])
        return {'msg': 'Categoria creada exitosamente'}, 201
    except:
        return {'msg': 'Ha ocurrido un error en el servidor'}

# ------------------------------------------------Configuracion-----------------------------------------


def filtroConfig(body):
    if not ('objConfig' in body):
        return body

    objConfiguracionJson = body['objConfig']
    ret = json.loads(objConfiguracionJson)
    return ret


@categoria.route('/categoria/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    data = request.get_json()
    body = filtroConfig(data)
    # -----CONFIGURACIONES-----
    try:
        # VALIDACIONES---
        if not ('id' in body and 'idCategoria' and 'nombre' in body and 'descripcion' in body and 'listarecursos'):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        if DB.verificacionID(body['idCategoria']):
            if DB.verificacionIDConfig(body.get('id')):
                return {'msg': 'Configuracion duplicada'}, 400

            # ---------------
            DB.addConfiguracion(
                body['id'], body['nombre'], body['descripcion'], body['listaRecursos'], body['idCategoria'])
            return {'msg': 'Configuracion creada exitosamente'}, 201
        return {'msg': 'la categoria no existe o no se encontro'}
    except:
        return {'msg': 'Ha ocurrido un error en el servidor'}