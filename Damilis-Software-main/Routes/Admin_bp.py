from flask import Blueprint
from Controllers.Admin_controller import AdminController


adm_bp = Blueprint('admin_bp', __name__)


# Listar todos los administradores
@adm_bp.route('/', methods=['GET'])
def listAdmins():
    return AdminController.ListAdmins()


# Crear un administrador
@adm_bp.route('/', methods=['POST'])
def createAdmin():
    return AdminController.create()


# Actualizar un administrador
@adm_bp.route('/', methods=['PUT'])
def updateAdmin():
    return AdminController.update()


# Eliminar un administrador
@adm_bp.route('/<int:id>', methods=['DELETE'])
def deleteAdmin(id):
    return AdminController.delete(id)


# Buscar administrador por ID de usuario
@adm_bp.route('/usuario/<user_id>', methods=['GET'])
def searchAdminByUserId(user_id):
    return AdminController.SearchByUserId(user_id)


# http://128.9.9.9/admins/
# http://128.9.9.9/admins/             (POST -> crear)
# http://128.9.9.9/admins/             (PUT  -> editar)
# http://128.9.9.9/admins/             (DELETE -> eliminar)
# http://128.9.9.9/admins/usuario/5