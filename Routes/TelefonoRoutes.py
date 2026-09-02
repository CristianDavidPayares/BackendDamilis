from flask import Blueprint
from Controllers.TelefonoController import TelefonoController

tel_bp = Blueprint('telefono_bp', __name__)


# Listar todos los teléfonos
@tel_bp.route('/', methods=['GET'])
def listarTelefonos():
    return TelefonoController.listar()


# Crear un teléfono
@tel_bp.route('/', methods=['POST'])
def crearTelefono():
    return TelefonoController.crear()


# Actualizar un teléfono
@tel_bp.route('/', methods=['PUT'])
def actualizarTelefono():
    return TelefonoController.actualizar()


# Eliminar un teléfono
@tel_bp.route('/<int:id>', methods=['DELETE'])
def eliminarTelefono(id):
    return TelefonoController.eliminar(id)


# Listar teléfonos por usuario
@tel_bp.route('/user/<int:user_id>', methods=['GET'])
def listarTelefonosPorUsuario(user_id):
    return TelefonoController.listarPorUsuario(user_id)