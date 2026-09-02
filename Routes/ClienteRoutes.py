from flask import Blueprint
from Controllers.ClienteController import ClienteController


cli_bp = Blueprint('cliente_bp', __name__)


# Listar todos los clientes
@cli_bp.route('/', methods=['GET'])
def listarClientes():
    return ClienteController.listar()


# Crear un cliente
@cli_bp.route('/', methods=['POST'])
def crearCliente():
    return ClienteController.crear()


# Actualizar un cliente
@cli_bp.route('/', methods=['PUT'])
def actualizarCliente():
    return ClienteController.actualizar()


# Eliminar un cliente
@cli_bp.route('/<int:id>', methods=['DELETE'])
def eliminarCliente(id):
    return ClienteController.eliminar(id)


# Cambiar estado de un cliente
@cli_bp.route('/estado', methods=['PUT'])
def cambiarEstadoCliente():
    return ClienteController.cambiarEstado()


# Buscar cliente por cédula
@cli_bp.route('/cedula/<per_cedula>', methods=['GET'])
def buscarClientePorCedula(per_cedula):
    return ClienteController.buscarPorCedula(per_cedula)


# Buscar cliente por ID de usuario
@cli_bp.route('/usuario/<user_id>', methods=['GET'])
def buscarClientePorUserId(user_id):
    return ClienteController.buscarPorUserId(user_id)