from flask import Blueprint
from Controllers.Admin_controller import (
    cntListAdmins,
    cntCreateAdmin,
    cntUpdateAdmin,
    cntDeleteAdmin,
    cntSearchByUserId
)

adm_bp = Blueprint('admin_bp', __name__)


@adm_bp.route('/', methods=['GET'])
def listAdmins():
    return cntListAdmins()


@adm_bp.route('/', methods=['POST'])
def createAdmin():
    return cntCreateAdmin()


@adm_bp.route('/', methods=['PUT'])
def updateAdmin():
    return cntUpdateAdmin()


@adm_bp.route('/<int:id>', methods=['DELETE'])
def deleteAdmin(id):
    return cntDeleteAdmin(id)


@adm_bp.route('/usuario/<user_id>', methods=['GET'])
def searchAdminByUserId(user_id):
    return cntSearchByUserId(user_id)


# http://128.9.9.9/admins/
# http://128.9.9.9/admins/             (POST -> crear)
# http://128.9.9.9/admins/             (PUT  -> editar)
# http://128.9.9.9/admins/             (DELETE -> eliminar)
# http://128.9.9.9/admins/usuario/5