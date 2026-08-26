
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


# http://128.9.9.9/pqrs/
# http://128.9.9.9/pqrs/            (POST -> crear)
# http://128.9.9.9/pqrs/            (PUT  -> editar)
# http://128.9.9.9/pqrs/            (DELETE -> eliminar)
# http://128.9.9.9/pqrs/cliente/7
# http://128.9.9.9/pqrs/responder   (PUT -> cambiar estado/responder)

