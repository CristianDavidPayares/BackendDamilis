from flask import Blueprint
from Controllers.User_controller import (
    cntListUsers,
    cntCreateUser,
    cntUpdateUser,
    cntDeleteUser,
    cntSearchByDoc
)

us_bp = Blueprint('user_bp', __name__)




@us_bp.route('/', methods=['GET'])
def listUsers():
    return cntListUsers()


@us_bp.route('/', methods=['POST'])
def createUser():
    return cntCreateUser()


@us_bp.route('/', methods=['PUT'])
def updateUser():
    return cntUpdateUser()


@us_bp.route("/<int:id>", methods=["DELETE"])
def deleteUser(id):
    return cntDeleteUser(id)


@us_bp.route('/search/<cedula>', methods=['GET'])
def searchUserByDoc(cedula):
    return cntSearchByDoc(cedula)


# http://128.9.9.9/users/
# http://128.9.9.9/users/          (POST -> crear)
# http://128.9.9.9/users/          (PUT  -> editar)
# http://128.9.9.9/users/          (DELETE -> eliminar)
# http://128.9.9.9/users/search/12345678