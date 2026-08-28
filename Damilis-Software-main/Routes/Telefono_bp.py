from flask import Blueprint
from Controllers.Telefono_controller import TelefonoController


tel_bp = Blueprint('telefono_bp', __name__)


# Listar todos los teléfonos
@tel_bp.route('/', methods=['GET'])
def listTelefonos():
    return TelefonoController.ListTelefonos()


# Crear un teléfono
@tel_bp.route('/', methods=['POST'])
def createTelefono():
    return TelefonoController.create()


# Actualizar un teléfono
@tel_bp.route('/', methods=['PUT'])
def updateTelefono():
    return TelefonoController.update()


# Eliminar un teléfono
@tel_bp.route('/<int:id>', methods=['DELETE'])
def deleteTelefono(id):
    return TelefonoController.delete(id)


# Listar teléfonos por usuario
@tel_bp.route('/user/<user_id>', methods=['GET'])
def listTelefonosByUser(user_id):
    return TelefonoController.ListTelefonosByUser(user_id)


# http://128.9.9.9/telefonos/
# http://128.9.9.9/telefonos/          (POST -> crear)
# http://128.9.9.9/telefonos/          (PUT  -> editar)
# http://128.9.9.9/telefonos/          (DELETE -> eliminar)
# http://128.9.9.9/telefonos/user/3