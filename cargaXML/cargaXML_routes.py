from flask import Blueprint, jsonify, request
import json
import re


cargaXML = Blueprint('cargaXML', __name__)

def dateCongiER(date):
    try:
        fechaER = re.findall("\d{2}/\d{2}/\d{4}", date)
        stringFecha = fechaER[0]
        return stringFecha
    except:
        print('ocurrio un error')

@cargaXML.route('/cargaXML/configuracion', methods=['POST'])
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
    data = {}  # Se crea un diccionario
    data['recursos'] = []  # Una lista con un identificador ->recursos
    data['categorias'] = []  # Una lista con un identificador ->categorias

    for a in range(len(listRecursos)):
        objRecurso = listRecursos[a]
        # Ingresando datos a lista que tiene el diccionario
        data['recursos'].append(json.loads(objRecurso))

    for b in range(len(listCategorias)):
        objCategoria = listCategorias[b]
        # Ingresando datos a lista que tiene el diccionario
        data['categorias'].append(json.loads(objCategoria))

    with open('./db/recursosYcategorias.json', 'w') as file:
        json.dump(data, file, indent=4)

    # CREAR DB DE LOS CLIENTES INGRESADAS CON ARCHIVO XML ---->
    dataClients = {}
    dataClients['clientes'] = []

    for c in range(len(listCliente)):
        objClient = listCliente[c]
        cliente = json.loads(objClient)
        dataClients['clientes'].append(cliente)

        # APLICACION DE ER PARA LA FECHA en formato 'dd/mm/yyyy' ----->
        for data in dataClients['clientes']:
            for instancia in data['listaInstancias']:
                fechaInicio = dateCongiER(instancia['fechaInicio'])
                fechaFinal = dateCongiER(instancia['fechaFinal'])
                instancia['fechaInicio'] = fechaInicio
                instancia['fechaFinal'] = fechaFinal

    with open('./db/clientes.json', 'w') as file:
        json.dump(dataClients, file, indent=4)

    return jsonify({'nombre de recurso': 'objRecurso.getName()'})


# -------------------------------------------------------------------------------------------------------
def dateConsumoER(date):
    try:
        fechaER = re.findall("\d{2}/\d{2}/\d{4} \d{2}:\d{2}", date)
        stringFecha = fechaER[0]
        return stringFecha
    except:
        print('ocurrio un error')

@cargaXML.route('/cargaXML/consumo', methods=['POST'])
def xmlConsumo():
    body = request.get_json()
    # -------------Consumo-----------------
    listConsumoJson = body['listConsumo']
    listConsumo = json.loads(listConsumoJson)

    # CREAR DB DE LOS CONSUMOS INGRESADAS CON ARCHIVO XML ---->
    data = {}  # Se crea un diccionario
    data['consumos'] = []  # Una lista con un identificador ->consumos

    for i in range(len(listConsumo)):
        objConsumo = listConsumo[i]
        consumo = json.loads(objConsumo)  # Deserealización

        # aplicando ER a la fecha en formato 'dd/mm/yyyy'
        fechaER = dateConsumoER(consumo.get('fechaHora'))
        # Modificando el atributo fechaHora del diccionario
        consumo['fechaHora'] = fechaER

        data['consumos'].append(consumo)  # Ingresando datos a la DB

    with open('./db/Consumos.json', 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({'msg': 'xml de consumo correctamente cargado'})