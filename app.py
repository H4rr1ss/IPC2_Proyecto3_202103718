from flask import Flask, jsonify
from flask_cors import CORS
from cargaXML.cargaXML_routes import cargaXML
from categorias.categorias_routes import categoria
from clientes.clientes_routes import cliente
from recursos.recursos_routes import recurso
from returnData.returnData_routes import data

app = Flask(__name__)
CORS(app)

prueba = {'msg': 'Esta es una api works!!'}

@app.route('/prueba', methods=["GET"])
def index():
    return jsonify(prueba)

app.register_blueprint(cargaXML)
app.register_blueprint(categoria)
app.register_blueprint(cliente)
app.register_blueprint(recurso)
app.register_blueprint(data)