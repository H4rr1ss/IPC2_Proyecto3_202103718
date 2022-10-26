from flask import Blueprint, jsonify, request
from db.database import DB
from xml.etree import ElementTree as ET
from .clases import Categoria, Recurso, Configuracion
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
    nit = body['nit']
    nameCliente = body['nameCliente']
    user = body['user']
    clave = body['clave']
    direccion = body['direccion']
    correo = body['correo']

    # ------INSTANCIA------
    idInstancia = body['idInstancia']
    idConfigInstancia = body['idConfigInstancia']
    nameInstancia = body['nameInstancia']
    fechaInicio = body['fechaInicio']
    estado = body['estado']
    fechaFinal = body['fechaFinal']

    print('\n')
    for i in range(len(listRecursos)):
        objRecurso = Recurso(**json.loads(listRecursos[i]))
        print('-----LISTA DE RECURSOS-- >')
        print('idRecurso: {} || nombreRecurso: {}\nabreviatura:{} || metrica: {}\ntipo: {} || valorXhora: {}\n'.format(objRecurso.id, objRecurso.name, objRecurso.abbreviation, objRecurso.metrics, objRecurso.type, objRecurso.price))
    print('------------------------------------------------')

    for j in range(len(listCategorias)):
        objCategoria = Categoria(**json.loads(listCategorias[j]))
        print('\n-----LISTA DE CATEGORIAS-- >')
        print('idCategoria: {} || nombreCategoria: {}\ndescripcion: {} || cargaTrabajo: {}\n'.format(objCategoria.id, objCategoria.name, objCategoria.description, objCategoria.workload))
        print('  -----LISTA CONFIGURACIONES')
        listConfigCategoria = json.loads(objCategoria.listConfiguration)
        for p in range(len(listConfigCategoria)):
            objConfigCate = Configuracion(**json.loads(listConfigCategoria[p]))
            print('  idConfig: {} || nombreConfig: {}\n  descripcionConfig: {} '.format(objConfigCate.id, objConfigCate.name, objConfigCate.description))

    return jsonify({'nombre de recurso': 'objRecurso.getName()'})


@client.route('/client/consumo', methods=['POST'])
def xmlConsumo():
    body = request.get_json()
    nit = body['nit']
    idInstancia = body['idInstancia']
    tiempo = body['tiempo']
    fechaHora = body['fechaHora']
    print(nit, idInstancia, tiempo, fechaHora)
    return jsonify({'msg': 'xml de consumo correctamente cargado'})