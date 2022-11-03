from audioop import add
from textwrap import indent
from turtle import width
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
                nameRecurso.append(id['nombre'])
                abreviatura.append(id['abreviatura'])
                metrica.append(id['metrica'])
                tipoRecurso.append(id['tipo'])
                precio.append(id['valorXhora'])
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
                nameCategoria.append(id['nombre'])
                descripcion.append(id['descripcion'])
                carga.append(id['cargaTrabajo'])
                for config in id['listaConfiguraciones']:
                    idConfigCategoria.append(config['id'])
                    nameConfig.append(config['nombre'])
                    descConfig.append(config['descripcion'])
                    for recurso in config['listaRecursos']:
                        idRecursoConfig.append(recurso['id'])
                        cantidad.append(recurso['cantidad'])
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
                nameClient.append(item['nombre'])
                user.append(item['usuario'])
                passw.append(item['clave'])
                address.append(item['direccion'])
                email.append(item['correoElectronico'])
                for sub in item['listaInstancias']:
                    idInstancia.append(sub['id'])
                    idConfigInstance.append(sub['idConfig'])
                    nameInstance.append(sub['nombre'])
                    initDate.append(sub['fechaInicio'])
                    status.append(sub['estado'])
                    finalDate.append(sub['fechaFinal'])
        return jsonify({'msg': 'Datos cargados', 'idRecurso': idRecurso, 'nombreRecurso': nameRecurso, 'abreviatura': abreviatura,
                        'metrica': metrica, 'tipo': tipoRecurso, 'precio': precio, 'idCategoria': idCategoria, 'nombreCategoria': nameCategoria, 'descripcion': descripcion, 'carga': carga, 'idConfigCategoria': idConfigCategoria,
                        'nombreConfig': nameConfig, 'descConfig': descConfig, 'idRecursoConfig': idRecursoConfig, 'cantidad': cantidad, 'nit': nit, 'nombreCliente': nameClient, 'usuario': user, 'clave': passw, 'direccion': address,
                        'email': email, 'idInstancia': idInstancia, 'idConfigInstancia': idConfigInstance, 'nombreInstancia': nameInstance, 'fechaInicio': initDate, 'estado': status, 'fechaFinal': finalDate})

    except:
        return jsonify({'msg': 'No existe base de datos o ha ocurrido un error'})


@data.route('/data/generarFactura', methods=['POST'])
def generarFactura():
    pass