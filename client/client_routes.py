from flask import Blueprint, jsonify, request
from db.database import DB

client = Blueprint('client', __name__)

#---------------------------------
# Actualmente los clientes se registran ingresando su 
# NOMBRE
# NIT
# DIRECCION FISICA
# EMAIL
@client.route('/client/register', methods=['POST'])
def createClient():
    body = request.get_json()
    
    nit = body['nit']
    name = body['name']
    address = body['address']

    if DB.createClient(name, nit, address) is True:
        return jsonify({'msg': 'Cliente ya existente!'})

    return jsonify({'msg': 'Se creo el cliente con exito!'})


#---------------------------------
# LUEGO DE VERIFICAR QUE EL USUARIO SI EXISTE EN EL SISTEMA
# DEBERÁ REDIRIGIR A OTRA PESTAÑA PARA SELECCIONAR SUS INSTANCIAS
@client.route('/client/login', methods=['POST'])
def userValidation():
    body = request.get_json()

    user = body['user']
    password = body['password']

    if DB.userValidation(user, password) is True:
        return jsonify({'msg': 'Bienvenido'})#Si se encuentra en la base de datos

    return jsonify({'msg': 'no existe.'})#Este usuario no existe.



# FALTA ARREGLAR LA SALIDA DE LOS JSON PERO PORQUE NO HE PUESTO LABELS EN EL HTML PARA QUE SE IMPRIMAN ALLÍ 
# ENTONCES POR ESO NO ESTAN ASÍ MEDIO FEO EL TEXTO QUE RETORNA