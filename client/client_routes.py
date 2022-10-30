from flask import Blueprint, jsonify, request
from db.database import DB
from xml.etree import ElementTree as ET
from .clases import Categoria, Cliente, Instancia, Recurso, Configuracion, Consumo
import json
import re


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

    # CREAR DB DE LOS RECURSOS Y CATEGORIAS INGRESADAS CON ARCHIVO XML ---->
    data = {}# Se crea un diccionario
    data['recursos'] = []# Una lista con un identificador ->recursos
    data['categorias'] = []# Una lista con un identificador ->categorias

    for a in range(len(listRecursos)):
        objRecurso = listRecursos[a]
        data['recursos'].append(json.loads(objRecurso))# Ingresando datos a lista que tiene el diccionario

    for b in range(len(listCategorias)):
        objCategoria = listCategorias[b]
        data['categorias'].append(json.loads(objCategoria))# Ingresando datos a lista que tiene el diccionario
    
    with open('./db/recursosYcategorias.json', 'w') as file:
        json.dump(data, file, indent=4)

    # CREAR DB DE LOS CLIENTES INGRESADAS CON ARCHIVO XML ---->
    dataClients = {}
    dataClients['clientes'] = []

    for c in range(len(listCliente)):
        objClient = listCliente[c]
        dataClients['clientes'].append(json.loads(objClient))# Ingresando datos a lista que tiene el diccionario

    with open('./db/clientes.json', 'w') as file:
        json.dump(dataClients, file, indent=4)


    return jsonify({'nombre de recurso': 'objRecurso.getName()'})






#-------------------------------------------------------------------------------------------------------
def dateER(date):
    try:
        fechaER = re.findall("\d{2}/\d{2}/\d{4} \d{2}:\d{2}", date)
        stringFecha = fechaER[0]
        return stringFecha
    except:
        print('ocurrio un error')

@client.route('/client/consumo', methods=['POST'])
def xmlConsumo():
    body = request.get_json()
    # -------------Consumo-----------------
    listConsumoJson = body['listConsumo']
    listConsumo = json.loads(listConsumoJson)

    # CREAR DB DE LOS CONSUMOS INGRESADAS CON ARCHIVO XML ---->
    data = {}# Se crea un diccionario
    data['consumos'] = []# Una lista con un identificador ->consumos

    for i in range(len(listConsumo)):
        objConsumo = listConsumo[i]
        consumo = json.loads(objConsumo)# Deserealización
        
        fechaER = dateER(consumo.get('fechaHora'))# aplicando ER a la fecha en formato 'dd/mm/yyyy'
        consumo['fechaHora'] = fechaER# Modificando el atributo fechaHora del diccionario

        data['consumos'].append(consumo)# Ingresando datos a la DB

    with open('./db/Consumos.json', 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({'msg': 'xml de consumo correctamente cargado'})
