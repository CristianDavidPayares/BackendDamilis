from flask import Blueprint
from Controllers.Compra_controller import (
    cntListCompras,
    cntCreateCompra,
    cntUpdateCompra,
    cntDeleteCompra,
    cntListComprasByCliente
)

comp_bp = Blueprint('compra_bp', __name__)


@comp_bp.route('/', methods=['GET'])
def listCompras():
    return cntListCompras()


@comp_bp.route('/', methods=['POST'])
def createCompra():
    return cntCreateCompra()


@comp_bp.route('/', methods=['PUT'])
def updateCompra():
    return cntUpdateCompra()


@comp_bp.route('/', methods=['DELETE'])
def deleteCompra():
    return cntDeleteCompra()


@comp_bp.route('/cliente/<cli_id>', methods=['GET'])
def listComprasByCliente(cli_id):
    return cntListComprasByCliente(cli_id)


# http://128.9.9.9/compras/
# http://128.9.9.9/compras/            (POST -> crear)
# http://128.9.9.9/compras/            (PUT  -> editar)
# http://128.9.9.9/compras/            (DELETE -> eliminar)
# http://128.9.9.9/compras/cliente/7