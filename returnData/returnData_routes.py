from flask import Blueprint, jsonify, request
from cargaXML.clases import Recurso, Consumo, Categoria, Cliente, Configuracion, Instancia, RecursoConfig
import json

data = Blueprint('data', __name__)


@data.route('/data/consultarDatos', methods=['GET'])
def consultarDatos():
    try:
        with open('./db/recursosYcategorias.json') as file:
            data = json.load(file)
            # ------------------------------Recursos-------------------------------
            idRecurso = []
            nameRecurso = []
            abreviatura = []
            metrica = []
            tipoRecurso = []
            precio = []
            for id in data['recursos']:
                idRecurso.append(id['id'])
                nameRecurso.append(id['name'])
                abreviatura.append(id['abbreviation'])
                metrica.append(id['metrics'])
                tipoRecurso.append(id['type'])
                precio.append(id['price'])
            objRecurso = Recurso(idRecurso, nameRecurso,
                                abreviatura, metrica, tipoRecurso, precio)
            objRecursoJson = json.dumps(objRecurso.__dict__)
            # ------------------------------Categorias------------------------
            idCategoria = []
            nameCategoria = []
            descripcion = []
            carga = []
            idConfigCategoria = []
            nameConfig = []
            descConfig = []
            idRecursoConfig = []
            cantidad = []
            for id in data['categorias']:
                idCategoria.append(id['id'])
                nameCategoria.append(id['name'])
                descripcion.append(id['description'])
                carga.append(id['workload'])
                for config in id['listConfiguration']:
                    idConfigCategoria.append(config['id'])
                    nameConfig.append(config['name'])
                    descConfig.append(config['description'])
                    for recurso in config['listRecursos']:
                        idRecursoConfig.append(recurso['id'])
                        cantidad.append(recurso['lot'])
                    objRecursoConf = RecursoConfig(idRecursoConfig, cantidad)
                    objRecursoConfJson = json.dumps(objRecursoConf.__dict__)
                objConfig = Configuracion(
                    idConfigCategoria, nameConfig, descConfig, objRecursoConfJson)
                objConfigJson = json.dumps(objConfig.__dict__)
            objCategoria = Categoria(
                idCategoria, nameCategoria, descripcion, carga, objConfigJson)
            objCategoriaJson = json.dumps(objCategoria.__dict__)
            # ------------------------------------Cliente--------------------------------------
            with open('./db/clientes.json') as file:
                data = json.load(file)
                nit = []
                nameClient = []
                user = []
                passw = []
                address = []
                email = []
                idInstancia = []
                idConfigInstance = []
                nameInstance = []
                initDate = []
                status = []
                finalDate = []
                for item in data['clientes']:
                    nit.append(item['nit'])
                    nameClient.append(item['name'])
                    user.append(item['user'])
                    passw.append(item['pasw'])
                    address.append(item['address'])
                    email.append(item['email'])

                    for sub in item['listInstance']:
                        idInstancia.append(sub['id'])
                        idConfigInstance.append(sub['idConfig'])
                        nameInstance.append(sub['name'])
                        initDate.append(sub['dateInitial'])
                        status.append(sub['status'])
                        finalDate.append(sub['dateFinal'])

        return jsonify({'idRecurso': idRecurso, 'nameRecurso': nameRecurso, 'abreviatura': abreviatura,
                        'metrica': metrica, 'tipo': tipoRecurso, 'precio': precio, 'idCategoria': idCategoria, 'nameCategoria': nameCategoria, 'descripcion': descripcion, 'carga': carga, 'idConfigCategoria': idConfigCategoria,
                        'nameConfig': nameConfig, 'descConfig': descConfig, 'idRecursoConfig': idRecursoConfig, 'lot': cantidad, 'nit': nit, 'nameClient': nameClient, 'user': user, 'pass': passw, 'address': address,
                        'email': email, 'idInstancia': idInstancia, 'idConfigInstance': idConfigInstance, 'nameInstancia': nameInstance, 'initDate': initDate, 'status': status, 'finalDate': finalDate})

    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500

@data.route('/data/generarFactura', methods=['POST'])
def generarFactura():
    pass