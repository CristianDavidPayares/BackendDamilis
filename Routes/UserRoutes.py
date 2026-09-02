from flask import Blueprint
from Controllers.UserController import UsuarioController

us_bp = Blueprint('user_bp', __name__)


# Listar usuarios
@us_bp.route('/', methods=['GET'])
def listarUsuarios():
    return UsuarioController.listar()


# Crear usuario
@us_bp.route('/', methods=['POST'])
def crearUsuario():
    return UsuarioController.crear()


# Actualizar usuario
@us_bp.route('/', methods=['PUT'])
def actualizarUsuario():
    return UsuarioController.actualizar()


# Eliminar usuario
@us_bp.route('/<int:id>', methods=['DELETE'])
def eliminarUsuario(id):
    return UsuarioController.eliminar(id)


# Buscar usuario por cédula
@us_bp.route('/search/<cedula>', methods=['GET'])
def buscarUsuarioPorCedula(cedula):
    return UsuarioController.buscarPorCedula(cedula)