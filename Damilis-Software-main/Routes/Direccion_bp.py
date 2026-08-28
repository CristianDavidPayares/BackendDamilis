from flask import Blueprint
from Controllers.Direccion_controller import DireccionController


dir_bp = Blueprint('direccion_bp', __name__)


# Listar todas las direcciones
@dir_bp.route('/', methods=['GET'])
def listDirecciones():
    return DireccionController.ListDirecciones()


# Crear una dirección
@dir_bp.route('/', methods=['POST'])
def createDireccion():
    return DireccionController.create()


# Actualizar una dirección
@dir_bp.route('/', methods=['PUT'])
def updateDireccion():
    return DireccionController.update()


# Eliminar una dirección
@dir_bp.route('/<int:id>', methods=['DELETE'])
def deleteDireccion(id):
    return DireccionController.delete(id)


# Listar direcciones por usuario
@dir_bp.route('/user/<user_id>', methods=['GET'])
def listDireccionesByUser(user_id):
    return DireccionController.ListDireccionesByUser(user_id)


# http://128.9.9.9/direcciones/
# http://128.9.9.9/direcciones/            (POST -> crear)
# http://128.9.9.9/direcciones/            (PUT  -> editar)
# http://128.9.9.9/direcciones/            (DELETE -> eliminar)
# http://128.9.9.9/direcciones/user/3