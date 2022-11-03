import requests
import json


class main_services:
    def rutaConfig(data):
        response = requests.post(
            'http://127.0.0.1:5000/cargaXML/configuracion', json=data)

        return json.loads(response.text)

    def rutaConsumo(data):
        response = requests.post(
            'http://127.0.0.1:5000/cargaXML/consumo', json=data)

        return json.loads(response.text)

    def Recursos(data):
        response = requests.post(
            'http://127.0.0.1:5000/recurso/crearRecurso', json=data)

        return json.loads(response.text)

    def categorias(data):
        response = requests.post(
            'http://127.0.0.1:5000/categoria/crearCategoria', json=data)

        return json.loads(response.text)

    def configuracion(data):
        response = requests.post(
            'http://127.0.0.1:5000/categoria/crearConfiguracion', json=data)

        return json.loads(response.text)

    def cliente(data):
        response = requests.post(
            'http://127.0.0.1:5000/cliente/crearCliente', json=data)

        return json.loads(response.text)

    def instancia(data):
        response = requests.post(
            'http://127.0.0.1:5000/cliente/crearInstancia', json=data)

        return json.loads(response.text)

    def cancelar(data):
        response = requests.post(
            'http://127.0.0.1:5000/cliente/cancelarInstancia', json=data)

        return json.loads(response.text)

    def consultar():
        response = requests.get(
            'http://127.0.0.1:5000/data/consultarDatos')

        return json.loads(response.text)
