from flask import Blueprint
from Controllers.Pqr_controller import PqrController


pqr_bp = Blueprint('pqr_bp', __name__)


# Listar todas las PQR
@pqr_bp.route('/', methods=['GET'])
def listPqrs():
    return PqrController.ListPqrs()


# Crear una PQR
@pqr_bp.route('/', methods=['POST'])
def createPqr():
    return PqrController.create()


# Actualizar una PQR
@pqr_bp.route('/', methods=['PUT'])
def updatePqr():
    return PqrController.update()


# Eliminar una PQR
@pqr_bp.route('/<int:id>', methods=['DELETE'])
def deletePqr(id):
    return PqrController.delete(id)


# Listar PQR por cliente
@pqr_bp.route('/cliente/<cli_id>', methods=['GET'])
def listPqrsByCliente(cli_id):
    return PqrController.ListPqrsByCliente(cli_id)


# Responder una PQR
@pqr_bp.route('/responder', methods=['PUT'])
def responderPqr():
    return PqrController.ResponderPqr()


# http://127.0.0.1:5000/pqrs/
# http://127.0.0.1:5000/pqrs/                 (POST -> crear)
# http://127.0.0.1:5000/pqrs/                 (PUT -> editar descripción)
# http://127.0.0.1:5000/pqrs/                 (DELETE -> eliminar)
# http://127.0.0.1:5000/pqrs/cliente/1        (GET -> PQRs de un cliente)
# http://127.0.0.1:5000/pqrs/responder        (PUT -> responder)