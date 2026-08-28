from flask import Blueprint
from Controllers.Correo_controller import CorreoController


cor_bp = Blueprint('correo_bp', __name__)


# Listar todos los correos
@cor_bp.route('/', methods=['GET'])
def listCorreos():
    return CorreoController.ListCorreos()


# Crear un correo
@cor_bp.route('/', methods=['POST'])
def createCorreo():
    return CorreoController.create()


# Actualizar un correo
@cor_bp.route('/', methods=['PUT'])
def updateCorreo():
    return CorreoController.update()


# Eliminar un correo
@cor_bp.route('/<int:id>', methods=['DELETE'])
def deleteCorreo(id):
    return CorreoController.delete(id)


# Listar correos por usuario
@cor_bp.route('/user/<user_id>', methods=['GET'])
def listCorreosByUser(user_id):
    return CorreoController.ListCorreosByUser(user_id)


# Buscar correo
@cor_bp.route('/buscar/<correo>', methods=['GET'])
def searchCorreo(correo):
    return CorreoController.SearchByCorreo(correo)

# http://128.9.9.9/correos/
# http://128.9.9.9/correos/            (POST -> crear)
# http://128.9.9.9/correos/            (PUT  -> editar)
# http://128.9.9.9/correos/            (DELETE -> eliminar)
# http://128.9.9.9/correos/user/3