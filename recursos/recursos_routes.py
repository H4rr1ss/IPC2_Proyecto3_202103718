from flask import Blueprint, jsonify, request
import json

recurso = Blueprint('recurso', __name__)

@recurso.route('/recurso/crearRecurso', methods=['POST'])
def crearRecurso():
    body = request.get_json()

    # -----RECURSOS-----
    objRecurso = body['objRecursos']
    objRecursoJson = json.loads(objRecurso)
    print(objRecursoJson)

    return jsonify({'nombre de recurso': 'objRecurso.getName()'})
