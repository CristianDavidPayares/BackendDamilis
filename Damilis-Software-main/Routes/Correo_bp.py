from flask import Blueprint
from Controllers.Correo_controller import (
    cntListCorreos,
    cntCreateCorreo,
    cntUpdateCorreo,
    cntDeleteCorreo,
    cntListCorreosByUser
)

cor_bp = Blueprint('correo_bp', __name__)


@cor_bp.route('/', methods=['GET'])
def listCorreos():
    return cntListCorreos()


@cor_bp.route('/', methods=['POST'])
def createCorreo():
    return cntCreateCorreo()


@cor_bp.route('/', methods=['PUT'])
def updateCorreo():
    return cntUpdateCorreo()


@cor_bp.route('/', methods=['DELETE'])
def deleteCorreo():
    return cntDeleteCorreo()


@cor_bp.route('/user/<user_id>', methods=['GET'])
def listCorreosByUser(user_id):
    return cntListCorreosByUser(user_id)


# http://128.9.9.9/correos/
# http://128.9.9.9/correos/            (POST -> crear)
# http://128.9.9.9/correos/            (PUT  -> editar)
# http://128.9.9.9/correos/            (DELETE -> eliminar)
# http://128.9.9.9/correos/user/3