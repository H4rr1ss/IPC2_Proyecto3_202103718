import json
from cargaXML.clases import Cliente, Recurso, Categoria, Configuracion, Consumo
import re
from datetime import datetime


class Database():

    # <VALIDACIONES>  [APARTADO RECURSOS]----------------------------

    def addRecurso(self, id, nombre, abreviatura, metrica, tipo, valorXhora):
        recurso = Recurso(id, nombre, abreviatura, metrica, tipo, valorXhora)

        with open('./db/recursosYcategorias.json', 'r+') as file:
            data = json.load(file)
            data['recursos'].append(recurso.__dict__)

        with open('./db/recursosYcategorias.json', 'r+') as file:
            json.dump(data, file, indent=4)

    # <VALIDACIONES>  [APARTADO CLIENTES]----------------------------
    def verificacionNIT(self, nitEntrada):
        with open('./db/clientes.json') as file:
            data = json.load(file)

            for client in data['clientes']:
                nit = client['nit']
                if nitEntrada == nit:
                    return True

        return False

    def agregarCliente(self, nit, name, user, passw, address, email, listInstance):
        cliente = Cliente(nit, name, user, passw, address, email, listInstance)

        with open('./db/clientes.json', 'r+') as file:
            data = json.load(file)
            data['clientes'].append(cliente.__dict__)

        with open('./db/clientes.json', 'r+') as file:
            json.dump(data, file, indent=4)

    # <VALIDACIONES>  [APARTADO INSTANCIAS]----------------------------
    def __fechaER(self, date):
        try:
            fechaER = re.findall("\d{2}/\d{2}/\d{4}", date)
            stringFecha = fechaER[0]
            return stringFecha
        except:
            print('ocurrio un error')

    def addInstanciaAcliente(self, nitCliente, instancia):
        with open('./db/clientes.json') as file:
            data = json.load(file)
            for client in data['clientes']:
                if nitCliente == client['nit']:
                    # APLICACION ER A LA FECHA
                    fechaInicial = self.__fechaER(instancia.fechaInicio)
                    instancia.fechaInicio = fechaInicial

                    fechaFinal = self.__fechaER(instancia.fechaFinal)
                    instancia.fechaFinal = fechaFinal

                    client['listaInstancias'].append(instancia.__dict__)

        with open('./db/clientes.json', 'w') as file:
            json.dump(data, file, indent=4)

    def verificarInstanciaExistente(self, nitCliente, idEntrada):
        with open('./db/clientes.json') as file:
            data = json.load(file)
            for client in data['clientes']:
                if nitCliente == client.get('nit'):
                    for intancia in client['listaInstancias']:
                        if intancia.get('id') == idEntrada:
                            return True
        return False

    # <VALIDACIONES>  [APARTADO CATEGORIAS]----------------------------
    def verificacionID(self, idEntrada):
        with open('./db/recursosYcategorias.json') as file:
            data = json.load(file)
            for categoria in data['categorias']:
                id = categoria['id']
                if idEntrada == id:
                    return True

        return False

    def addCategoria(self, id, nombre, desc, cargaT, listConfig):
        categoria = Categoria(id, nombre, desc, cargaT, listConfig)

        with open('./db/recursosYcategorias.json', 'r+') as file:
            data = json.load(file)
            data['categorias'].append(categoria.__dict__)

        with open('./db/recursosYcategorias.json', 'r+') as file:
            json.dump(data, file, indent=4)

    # <VALIDACIONES>  [APARTADO CONFIGURACIONES]----------------------------
    def verificacionIDConfig(self, idEntrada):
        with open('./db/recursosYcategorias.json') as file:
            data = json.load(file)
            for categoria in data['categorias']:
                for config in categoria['listaConfiguraciones']:
                    id = config['id']
                    if idEntrada == id:
                        return True

        return False

    def addConfiguracion(self, idCate, idC, nombre, descripcion, listaRecursos):
        configuracion = Configuracion(idC, nombre, descripcion, listaRecursos)

        with open('./db/recursosYcategorias.json', 'r+') as file:
            data = json.load(file)

            for categoria in data['categorias']:
                if idCate == categoria['id']:
                    categoria['listaConfiguraciones'].append(
                        configuracion.__dict__)

        with open('./db/recursosYcategorias.json', 'r+') as file:
            json.dump(data, file, indent=4)

    # <VALIDACIONES>  [APARTADO CANCELAR INSTANCIAS]----------------------------
    def modificacionesCliente(self, nitCliente, idInstancia):
        with open('./db/clientes.json') as file:
            data = json.load(file)

            for client in data['clientes']:
                if nitCliente == client.get('nit'):
                    for instancia in client['listaInstancias']:
                        if instancia.get('id') == idInstancia:
                            print('estado de la instancia: {}'.format(instancia['estado']))

                            config = instancia.get('idConfig')
                            if instancia.get('estado').lower() == 'cancelada':
                                return None
                            else:
                                instancia['estado'] = 'Cancelada'
                                now = datetime.now()

                                fechaHora = '{}/{}/{} {}:{}'.format(now.day, now.month, now.year, now.minute, now.second)
                                fechaFinal = '{}/{}/{}'.format(now.day, now.month, now.year)
                                
                                instancia['fechaFinal'] = fechaFinal
        with open('./db/clientes.json', 'w') as file:
            json.dump(data, file, indent=4)

        return fechaHora, config

    def agregarConsumo(self, nitCliente, idInstancia, tiempo, fechaHora):
        consumo = Consumo(nitCliente, idInstancia, tiempo, fechaHora)
       
        with open('./db/Consumos.json', 'r+') as file:
            data = json.load(file)
            data['consumos'].append(consumo.__dict__)
        
        with open('./db/Consumos.json', 'w') as file:
            json.dump(data, file, indent=4)

    def buscarRecursoo(self, id):
        with open('./db/recursosYcategorias.json') as file:
            data = json.load(file)

            for recurso in data['recursos']:
                if id == recurso['id']:
                    valor = recurso['valorXhora']
                    
                    return valor

    def calculoTiempo(self, idConfig):
        total = 0
        with open('./db/recursosYcategorias.json') as file:
            data = json.load(file)

            for categoria in data['categorias']:
                for configuracion in categoria['listaConfiguraciones']:
                    if configuracion['id'] == idConfig:
                        for recurso in configuracion['listaRecursos']:
                            cantidad = int(recurso['cantidad'])
                            valor = self.buscarRecursoo(recurso['id'])
                            total = str(cantidad*float(valor))

                            return total

DB = Database()
