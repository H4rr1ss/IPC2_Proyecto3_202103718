import json
from .clases import Recurso, RecursoConfig, Configuracion, Categoria, Instancia, Cliente, Consumo


def handle_uploaded_file(f):
    with open('main/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def xmlConfig(rutaConfig):
    # -----------------------------Listas Archivo de configuracion------------------------------------
    # RECURSOS
    listRecursos = []
    idRecurso = ''
    nameRecurso = ''
    abreviatura = ''
    metricaRecurso = ''
    tipoRecurso = ''
    precioRecurso = ''

    # CATEGORIA
    listCategoria = []
    idCategoria = ''
    nameCategoria = ''
    descCategoria = ''
    cargaCategoria = ''
    # CONFIGURACION DE LA CATEGORIA
    idConfig = ''
    nameConfig = ''
    descConfig = ''
    # RECURSOS DE LA CONFIGURACION
    idRecursoConfig = ''
    recursoConfig = ''

    # CLIENTE
    listCliente = []
    nit = ''
    nameCliente = ''
    user = ''
    clave = ''
    direccion = ''
    correo = ''
    # INSTANCIAS DEL CLIENTE
    idInstancia = ''
    idConfigInstancia = ''
    nameInstancia = ''
    fechaInicio = ''
    estado = ''
    fechaFinal = ''

# -----------------------------------Lectura Archivo de configuracion------------------------------------------
    try:
        for configuracion in rutaConfig:
            for listaRecurso in configuracion:
                if listaRecurso.tag == 'recurso':
                    idRecurso = listaRecurso.get('id')
                    for recurso in listaRecurso:
                        if recurso.tag == 'nombre':
                            nameRecurso = recurso.text
                        elif recurso.tag == 'abreviatura':
                            abreviatura = recurso.text
                        elif recurso.tag == 'metrica':
                            metricaRecurso = recurso.text
                        elif recurso.tag == 'tipo':
                            tipoRecurso = recurso.text
                        elif recurso.tag == 'valorXhora':
                            precioRecurso = recurso.text
                    # SERIALIZACIÓN
                    objRecurso = Recurso(
                        idRecurso, nameRecurso, abreviatura, metricaRecurso, tipoRecurso, precioRecurso)
                    objRecursoJson = json.dumps(objRecurso.__dict__, indent=4)
                    # print(objRecursoJson)
                    listRecursos.append(objRecursoJson)
                    cantidadRecursos = len(listRecursos)
                    listRecursosJson = json.dumps(listRecursos)

            for ListaCategorias in configuracion:
                if ListaCategorias.tag == 'categoria':
                    idCategoria = ListaCategorias.get('id')
                    listConfigCategoria = []
                    for categoria in ListaCategorias:
                        if categoria.tag == 'nombre':
                            nameCategoria = categoria.text
                        elif categoria.tag == 'descripcion':
                            descCategoria = categoria.text
                        elif categoria.tag == 'cargaTrabajo':
                            cargaCategoria = categoria.text
                        for ListaConfig in categoria:
                            idConfig = ListaConfig.get('id')
                            listRecursosConfiguracion = []
                            for config in ListaConfig:
                                if config.tag == 'nombre':
                                    nameConfig = config.text
                                elif config.tag == 'descripcion':
                                    descConfig = config.text
                                for recursosConfig in config:
                                    idRecursoConfig = recursosConfig.get('id')
                                    if recursosConfig.tag == 'recurso':
                                        recursoConfig = recursosConfig.text

                                    objRecursoConfig = RecursoConfig(
                                        idRecursoConfig, recursoConfig)
                                    listRecursosConfiguracion.append(
                                        objRecursoConfig.__dict__)

                            objConfig = Configuracion(
                                idConfig, nameConfig, descConfig, listRecursosConfiguracion)
                            objConfigJSON = json.dumps(
                                objConfig.__dict__, indent=4)
                            listConfigCategoria.append(objConfig.__dict__)
                            print(objConfig)
                            print('\n\n')
                            print(objConfigJSON)

                    objCategoria = Categoria(
                        idCategoria, nameCategoria, descCategoria, cargaCategoria, listConfigCategoria)
                    objCategoriaJSON = json.dumps(objCategoria.__dict__)
                    listCategoria.append(objCategoriaJSON)
                    cantidadCategoria = len(listCategoria)
                    listCategoriaJSON = json.dumps(listCategoria)

            for ListaClientes in configuracion:
                if ListaClientes.tag == 'cliente':
                    nit = ListaClientes.get('nit')
                    for cliente in ListaClientes:
                        if cliente.tag == 'nombre':
                            nameCliente = cliente.text
                        elif cliente.tag == 'usuario':
                            user = cliente.text
                        elif cliente.tag == 'clave':
                            clave = cliente.text
                        elif cliente.tag == 'direccion':
                            direccion = cliente.text
                        elif cliente.tag == 'correoElectronico':
                            correo = cliente.text
                        for listaInstancias in cliente:
                            idInstancia = listaInstancias.get('id')
                            listaInstancia = []
                            for instancia in listaInstancias:
                                if instancia.tag == 'idConfiguracion':
                                    idConfigInstancia = instancia.text
                                elif instancia.tag == 'nombre':
                                    nameInstancia = instancia.text
                                elif instancia.tag == 'fechaInicio':
                                    fechaInicio = instancia.text
                                elif instancia.tag == 'estado':
                                    estado = instancia.text
                                elif instancia.tag == 'fechaFinal':
                                    fechaFinal = instancia.text
                            objInstancia = Instancia(
                                idInstancia, idConfigInstancia, nameInstancia, fechaInicio, estado, fechaFinal)
                            objInstanciaJSON = json.dumps(
                                objInstancia.__dict__)
                            listaInstancia.append(objInstancia.__dict__)
                            listaInstanciaJSON = json.dumps(listaInstancia)

                    objCliente = Cliente(
                        nit, nameCliente, user, clave, direccion, correo, listaInstancia)
                    objClienteJSON = json.dumps(objCliente.__dict__)
                    listCliente.append(objClienteJSON)
                    cantidadClientes = len(listCliente)
                    listClienteJSON = json.dumps(listCliente)

        return listRecursosJson, listCategoriaJSON, listClienteJSON, cantidadRecursos, cantidadCategoria, cantidadClientes

    except:
        return 'Ha ocurrido un error'


def readConsumo(rutaConsumo):
    listConsumo = []
    nit = ''
    idInstancia = ''
    tiempo = ''
    fechaHora = ''

    for listadoConsumo in rutaConsumo:
        if listadoConsumo.tag == 'consumo':
            nit = listadoConsumo.get('nitCliente')
            idInstancia = listadoConsumo.get('idInstancia')
            for consumo in listadoConsumo:
                if consumo.tag == 'tiempo':
                    tiempo = consumo.text
                elif consumo.tag == 'fechaHora':
                    fechaHora = consumo.text
            objConsumo = Consumo(nit, idInstancia, tiempo, fechaHora)
            objConsumoJson = json.dumps(objConsumo.__dict__)
            listConsumo.append(objConsumoJson)
            cantidadConsumo = len(listadoConsumo)
            listConsumoJson = json.dumps(listConsumo)

    return listConsumoJson, cantidadConsumo
