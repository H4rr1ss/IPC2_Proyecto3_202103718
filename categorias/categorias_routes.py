from flask import Blueprint, jsonify, request
import json

categoria = Blueprint('categoria', __name__)

@categoria.route('/categoria/crearCategoria', methods=['POST'])
def crearCategoria():
    body = request.get_json()
    # -----CATEGORIAS-----
    objCategoriasJson = body['objCategoria']
    objCategorias = json.loads(objCategoriasJson)
    print(objCategorias)
    return jsonify({'msg': 'ruta de categoria'})

@categoria.route('/categoria/crearConfiguracion', methods=['POST'])
def crearConfiguracion():
    body = request.get_json()
    objConfigJson = body['objConfig']
    objConfig = json.loads(objConfigJson)
    print(objConfig)
    return jsonify({'msg': 'ruta de creacion de configuracion '})