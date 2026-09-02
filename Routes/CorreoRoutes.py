from flask import Blueprint
from Controllers.CorreoController import CorreoController


cor_bp = Blueprint('correo_bp', __name__)


# Listar todos los correos
@cor_bp.route('/', methods=['GET'])
def listarCorreos():
    return CorreoController.listar()


# Crear un correo
@cor_bp.route('/', methods=['POST'])
def crearCorreo():
    return CorreoController.crear()


# Actualizar un correo
@cor_bp.route('/', methods=['PUT'])
def actualizarCorreo():
    return CorreoController.actualizar()


# Eliminar un correo
@cor_bp.route('/<int:id>', methods=['DELETE'])
def eliminarCorreo(id):
    return CorreoController.eliminar(id)


# Listar correos por usuario
@cor_bp.route('/user/<int:user_id>', methods=['GET'])
def listarCorreosPorUsuario(user_id):
    return CorreoController.listarPorUsuario(user_id)


# Buscar correo por dirección
@cor_bp.route('/buscar/<correo>', methods=['GET'])
def buscarCorreo(correo):
    return CorreoController.buscarPorCorreo(correo)