from flask import Blueprint, jsonify, request
from db.database import DB
from xml.etree import ElementTree as ET
from .clases import Categoria, Cliente, Instancia, Recurso, Configuracion, Consumo
import json


client = Blueprint('client', __name__)


@client.route('/client/configuracion', methods=['POST'])
def rutaConfig():
    body = request.get_json()

    # -----RECURSOS-----
    listRecursoJson = body['listRecursosJson']
    listRecursos = json.loads(listRecursoJson)

    # -----CATEGORIAS-----
    listCategoriasJson = body['listCategoriasJSON']
    listCategorias = json.loads(listCategoriasJson)

    # ------CLIENTE------
    listClientesJson = body['listaClientes']
    listCliente = json.loads(listClientesJson)

    data = {}
    data['recursos'] = []
    data['categorias'] = []

    for i in range(len(listRecursos)):
        objRecurso = listRecursos[i]
        print(json.loads(objRecurso))
        data['recursos'].append(json.loads(objRecurso))

    for j in range(len(listCategorias)):
        objCategoria = listCategorias[j]
        data['categorias'].append(json.loads(objCategoria))
    
    with open('./db/ClientAndCategoria.json', 'w') as file:
        json.dump(data, file, indent=4)


    return jsonify({'nombre de recurso': 'objRecurso.getName()'})












@client.route('/client/consumo', methods=['POST'])
def xmlConsumo():
    body = request.get_json()
    # -------------Consumo-----------------
    listConsumoJson = body['listConsumo']
    listConsumo = json.loads(listConsumoJson)


    data = {}
    data['consumos'] = []

    for i in range(len(listConsumo)):
        objConsumo = listConsumo[i]
        print(json.loads(objConsumo))
        data['consumos'].append(json.loads(objConsumo))


    with open('./db/Consumos.json', 'w') as file:
        json.dump(data, file, indent=4)


    return jsonify({'msg': 'xml de consumo correctamente cargado'})
