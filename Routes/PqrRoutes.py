from flask import Blueprint
from Controllers.PqrController import PqrController

pqr_bp = Blueprint('pqr_bp', __name__)


# Listar todas las PQR
@pqr_bp.route('/', methods=['GET'])
def listarPqrs():
    return PqrController.listar()


# Crear una PQR
@pqr_bp.route('/', methods=['POST'])
def crearPqr():
    return PqrController.crear()


# Actualizar una PQR
@pqr_bp.route('/', methods=['PUT'])
def actualizarPqr():
    return PqrController.actualizar()


# Eliminar una PQR
@pqr_bp.route('/<int:id>', methods=['DELETE'])
def eliminarPqr(id):
    return PqrController.eliminar(id)


# Listar PQR por cliente
@pqr_bp.route('/cliente/<int:cli_id>', methods=['GET'])
def listarPqrsPorCliente(cli_id):
    return PqrController.listarPorCliente(cli_id)


# Responder una PQR
@pqr_bp.route('/responder', methods=['PUT'])
def responderPqr():
    return PqrController.responder()