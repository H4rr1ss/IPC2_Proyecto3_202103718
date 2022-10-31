from flask import Blueprint, jsonify, request
import json

data = Blueprint('data', __name__)

@data.route('/data/consultarDatos', methods=['GET'])
def consultarDatos():
    pass

@data.route('/data/generarFactura', methods=['POST'])
def generarFactura():
    pass