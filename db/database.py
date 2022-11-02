import json
from cargaXML.clases import Cliente

class Database():

    # -------- CLIENTE --------
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

        with open('./db/clientes.json', 'w') as file:
            json.dump(data, file, indent=4)


DB = Database()