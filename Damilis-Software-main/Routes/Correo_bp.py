from flask import Blueprint
<<<<<<< Updated upstream
from Controllers.Correo_controller import (
    cntListCorreos,
    cntCreateCorreo,
    cntUpdateCorreo,
    cntDeleteCorreo,
    cntListCorreosByUser
)
=======
from Controllers.Correo_controller import CorreoController
>>>>>>> Stashed changes

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


<<<<<<< Updated upstream
@cor_bp.route('/', methods=['DELETE'])
def deleteCorreo():
    return cntDeleteCorreo()
=======
@cor_bp.route('/<id>', methods=['DELETE'])
def deleteCorreo(id):
    return CorreoController.delete(id)
>>>>>>> Stashed changes


@cor_bp.route('/user/<user_id>', methods=['GET'])
def listCorreosByUser(user_id):
    return cntListCorreosByUser(user_id)


# http://128.9.9.9/correos/
# http://128.9.9.9/correos/            (POST -> crear)
# http://128.9.9.9/correos/            (PUT  -> editar)
# http://128.9.9.9/correos/<id>        (DELETE -> eliminar)
# http://128.9.9.9/correos/user/3