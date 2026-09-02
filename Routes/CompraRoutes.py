from flask import Blueprint
from Controllers.CompraController import CompraController


comp_bp = Blueprint('compra_bp', __name__)


# Listar todas las compras
@comp_bp.route('/', methods=['GET'])
def listarCompras():
    return CompraController.listar()


# Crear una compra
@comp_bp.route('/', methods=['POST'])
def crearCompra():
    return CompraController.crear()


# Actualizar una compra
@comp_bp.route('/', methods=['PUT'])
def actualizarCompra():
    return CompraController.actualizar()


# Eliminar una compra
@comp_bp.route('/<int:id>', methods=['DELETE'])
def eliminarCompra(id):
    return CompraController.eliminar(id)


# Listar compras por cliente
@comp_bp.route('/cliente/<int:cli_id>', methods=['GET'])
def listarComprasPorCliente(cli_id):
    return CompraController.listarPorCliente(cli_id)


# http://128.9.9.9/compras/
# http://128.9.9.9/compras/             (POST -> crear)
# http://128.9.9.9/compras/             (PUT -> actualizar)
# http://128.9.9.9/compras/<id>         (DELETE -> eliminar)
# http://128.9.9.9/compras/cliente/7    (GET -> listar por cliente)