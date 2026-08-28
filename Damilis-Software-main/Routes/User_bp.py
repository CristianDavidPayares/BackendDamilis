from flask import Blueprint
from Controllers.User_controller import UserController


us_bp = Blueprint('user_bp', __name__)


# Listar usuarios
@us_bp.route('/', methods=['GET'])
def listUsers():
    return UserController.ListUsers()


# Crear usuario
@us_bp.route('/', methods=['POST'])
def createUser():
    return UserController.create()


# Actualizar usuario
@us_bp.route('/', methods=['PUT'])
def updateUser():
    return UserController.update()


# Eliminar usuario
@us_bp.route('/<int:id>', methods=['DELETE'])
def deleteUser(id):
    return UserController.delete(id)


# Buscar usuario por cédula
@us_bp.route('/search/<cedula>', methods=['GET'])
def searchUserByDoc(cedula):
    return UserController.SearchByDoc(cedula)

# http://128.9.9.9/users/
# http://128.9.9.9/users/          (POST -> crear)
# http://128.9.9.9/users/          (PUT  -> editar)
# http://128.9.9.9/users/          (DELETE -> eliminar)
# http://128.9.9.9/users/search/12345678