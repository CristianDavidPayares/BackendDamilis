from flask import Blueprint
from Controllers.DireccionController import DireccionController


dir_bp = Blueprint('direccion_bp', __name__)


# Listar todas las direcciones
@dir_bp.route('/', methods=['GET'])
def listarDirecciones():
    return DireccionController.listar()


# Crear una dirección
@dir_bp.route('/', methods=['POST'])
def crearDireccion():
    return DireccionController.crear()


# Actualizar una dirección
@dir_bp.route('/', methods=['PUT'])
def actualizarDireccion():
    return DireccionController.actualizar()


# Eliminar una dirección
@dir_bp.route('/<int:id>', methods=['DELETE'])
def eliminarDireccion(id):
    return DireccionController.eliminar(id)


# Listar direcciones por usuario
@dir_bp.route('/user/<int:user_id>', methods=['GET'])
def listarDireccionesPorUsuario(user_id):
    return DireccionController.listarPorUsuario(user_id)