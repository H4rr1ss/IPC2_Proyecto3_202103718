from flask import Blueprint, jsonify, request
import json
from db.database import DB

recurso = Blueprint('recurso', __name__)


def filtro(body):
    if not ('objRecursos' in body):
        return body

    objRecursosJson = body['objRecursos']
    ret = json.loads(objRecursosJson)
    return ret


@recurso.route('/recurso/crearRecurso', methods=['POST'])
def crearRecurso():
    data = request.get_json()
    # -----RECURSOS-----
    body = filtro(data)

    try:
        # VALIDACIONES---
        if not ('id' in body and 'nombre' in body and 'abreviatura' in body and 'metrica' in body and 'tipo' in body and 'valorXhora' in body):
            return {'msg': 'Faltan campos en el cuerpo de la petición'}, 400
        # ---------------

        DB.addRecurso(body['id'], body['nombre'], body['abreviatura'],
                      body['metrica'], body['tipo'], body['valorXhora'])
        return {'msg': 'Recurso creado exitosamente'}, 201
    except:
        return {'msg': 'Ocurrio un error en el servidor'}, 500