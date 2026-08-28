from flask import Blueprint
from Controllers.Cliente_controller import ClienteController


cli_bp = Blueprint('cliente_bp', __name__)


# Listar todos los clientes
@cli_bp.route('/', methods=['GET'])
def listClientes():
    return ClienteController.ListClientes()


# Crear un cliente
@cli_bp.route('/', methods=['POST'])
def createCliente():
    return ClienteController.create()


# Actualizar un cliente
@cli_bp.route('/', methods=['PUT'])
def updateCliente():
    return ClienteController.update()


# Eliminar un cliente
@cli_bp.route('/<int:id>', methods=['DELETE'])
def deleteCliente(id):
    return ClienteController.delete(id)


# Cambiar estado de un cliente
@cli_bp.route('/estado', methods=['PUT'])
def cambiarEstadoCliente():
    return ClienteController.CambiarEstado()


# Buscar cliente por cédula
@cli_bp.route('/cedula/<per_cedula>', methods=['GET'])
def searchClienteByCedula(per_cedula):
    return ClienteController.SearchByCedula(per_cedula)


# Buscar cliente por ID de usuario
@cli_bp.route('/usuario/<user_id>', methods=['GET'])
def searchClienteByUserId(user_id):
    return ClienteController.SearchByUserId(user_id)

# http://128.9.9.9/clientes/
# http://128.9.9.9/clientes/               (POST -> crear)
# http://128.9.9.9/clientes/               (PUT  -> editar preferencias)
# http://128.9.9.9/clientes/               (DELETE -> eliminar)
# http://128.9.9.9/clientes/estado         (PUT -> cambia CLI_ESTADO)
# http://128.9.9.9/clientes/cedula/123456
# http://128.9.9.9/clientes/usuario/5