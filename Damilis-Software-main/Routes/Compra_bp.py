from flask import Blueprint
from Controllers.Compra_controller import CompraController


comp_bp = Blueprint('compra_bp', __name__)


# Listar todas las compras
@comp_bp.route('/', methods=['GET'])
def listCompras():
    return CompraController.ListCompras()


# Crear una compra
@comp_bp.route('/', methods=['POST'])
def createCompra():
    return CompraController.create()


# Actualizar una compra
@comp_bp.route('/', methods=['PUT'])
def updateCompra():
    return CompraController.update()


# Eliminar una compra
@comp_bp.route('/<int:id>', methods=['DELETE'])
def deleteCompra(id):
    return CompraController.delete(id)


# Listar compras por cliente
@comp_bp.route('/cliente/<cli_id>', methods=['GET'])
def listComprasByCliente(cli_id):
    return CompraController.ListComprasByCliente(cli_id)


# http://128.9.9.9/compras/
# http://128.9.9.9/compras/            (POST -> crear)
# http://128.9.9.9/compras/            (PUT  -> editar)
# http://128.9.9.9/compras/            (DELETE -> eliminar)
# http://128.9.9.9/compras/cliente/7