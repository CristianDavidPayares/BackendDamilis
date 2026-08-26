from flask import Blueprint
from Controllers.Cliente_controller import (
    cntListClientes,
    cntCreateCliente,
    cntUpdateCliente,
    cntDeleteCliente,
    cntCambiarEstado,
    cntSearchByCedula,
    cntSearchByUserId
)

cli_bp = Blueprint('cliente_bp', __name__)


@cli_bp.route('/', methods=['GET'])
def listClientes():
    return cntListClientes()


@cli_bp.route('/', methods=['POST'])
def createCliente():
    return cntCreateCliente()


@cli_bp.route('/', methods=['PUT'])
def updateCliente():
    return cntUpdateCliente()

@cli_bp.route('/<int:id>', methods=['DELETE'])
def deleteCliente(id):
    return cntDeleteCliente(id)

@cli_bp.route('/estado', methods=['PUT'])
def cambiarEstadoCliente():
    return cntCambiarEstado()


@cli_bp.route('/cedula/<per_cedula>', methods=['GET'])
def searchClienteByCedula(per_cedula):
    return cntSearchByCedula(per_cedula)


@cli_bp.route('/usuario/<user_id>', methods=['GET'])
def searchClienteByUserId(user_id):
    return cntSearchByUserId(user_id)


# http://128.9.9.9/clientes/
# http://128.9.9.9/clientes/               (POST -> crear)
# http://128.9.9.9/clientes/               (PUT  -> editar preferencias)
# http://128.9.9.9/clientes/               (DELETE -> eliminar)
# http://128.9.9.9/clientes/estado         (PUT -> cambia CLI_ESTADO)
# http://128.9.9.9/clientes/cedula/123456
# http://128.9.9.9/clientes/usuario/5