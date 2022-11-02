from flask import Blueprint, jsonify, request
import json
from db.database import DB

categoria = Blueprint('categoria', __name__)

def filtro(body):
    if not('objCategoria' in body):
        return body
    elif not('objConfig' in body):
        return body

    objClientesJson = body['objCliente']#PENDIENTE DE MODIFICAR (FRONT)
    ret = json.loads(objClientesJson)
    return ret

@categoria.route('/categoria/crearCategoria', methods=['POST'])
def crearCategoria():
    data = request.get_json()
    # -----CATEGORIAS-----
    body = filtro(data)
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


@categoria.route('/categoria/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    data = request.get_json()
    # -----CATEGORIAS-----
    body = filtro(data)
    try:
        # VALIDACIONES---
        if not ('id' in body and 'nombre' in body and 'descripcion' in body and 'listaRecursos'):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400

        #if DB.verificacionCategoriaID(body.get('id')):
            #return {'msg': 'Categoria duplicada'}, 400
        # ---------------

        #DB.addCategoria(body['id'], body['nombre'], body['descripcion'], body['cargaTrabajo'], body['listaConfiguraciones'])
        return {'msg': 'Categoria creada exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500

    body = request.get_json()
    objConfigJson = body['objConfig']
    objConfig = json.loads(objConfigJson)
    print(objConfig)
    return jsonify({'msg': 'ruta de creacion de configuracion '})