from flask import Blueprint
from Controllers.Telefono_controller import (
    cntListTelefonos,
    cntCreateTelefono,
    cntUpdateTelefono,
    cntDeleteTelefono,
    cntListTelefonosByUser
)

tel_bp = Blueprint('telefono_bp', __name__)


@tel_bp.route('/', methods=['GET'])
def listTelefonos():
    return cntListTelefonos()


@tel_bp.route('/', methods=['POST'])
def createTelefono():
    return cntCreateTelefono()


@tel_bp.route('/', methods=['PUT'])
def updateTelefono():
    return cntUpdateTelefono()


@tel_bp.route('/', methods=['DELETE'])
def deleteTelefono():
    return cntDeleteTelefono()


@tel_bp.route('/user/<user_id>', methods=['GET'])
def listTelefonosByUser(user_id):
    return cntListTelefonosByUser(user_id)


# http://128.9.9.9/telefonos/
# http://128.9.9.9/telefonos/          (POST -> crear)
# http://128.9.9.9/telefonos/          (PUT  -> editar)
# http://128.9.9.9/telefonos/          (DELETE -> eliminar)
# http://128.9.9.9/telefonos/user/3