from flask import Blueprint

from Controllers.Pqr_controller import (
    cntListPqrs,
    cntCreatePqr,
    cntUpdatePqr,
    cntDeletePqr,
    cntListPqrsByCliente,
    cntResponderPqr
)


pqr_bp = Blueprint('pqr_bp', __name__)


@pqr_bp.route('/', methods=['GET'])
def listPqrs():
    return cntListPqrs()


@pqr_bp.route('/', methods=['POST'])
def createPqr():
    return cntCreatePqr()


@pqr_bp.route('/', methods=['PUT'])
def updatePqr():
    return cntUpdatePqr()


@pqr_bp.route('/', methods=['DELETE'])
def deletePqr():
    return cntDeletePqr()


@pqr_bp.route('/cliente/<cli_id>', methods=['GET'])
def listPqrsByCliente(cli_id):
    return cntListPqrsByCliente(cli_id)


@pqr_bp.route('/responder', methods=['PUT'])
def responderPqr():
    return cntResponderPqr()


# http://127.0.0.1:5000/pqrs/
# http://127.0.0.1:5000/pqrs/                 (POST -> crear)
# http://127.0.0.1:5000/pqrs/                 (PUT -> editar descripción)
# http://127.0.0.1:5000/pqrs/                 (DELETE -> eliminar)
# http://127.0.0.1:5000/pqrs/cliente/1        (GET -> PQRs de un cliente)
# http://127.0.0.1:5000/pqrs/responder        (PUT -> responder)