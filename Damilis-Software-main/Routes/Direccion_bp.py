from flask import Blueprint
from Controllers.Direccion_controller import (
    cntListDirecciones,
    cntCreateDireccion,
    cntUpdateDireccion,
    cntDeleteDireccion,
    cntListDireccionesByUser
)

dir_bp = Blueprint('direccion_bp', __name__)


@dir_bp.route('/', methods=['GET'])
def listDirecciones():
    return cntListDirecciones()


@dir_bp.route('/', methods=['POST'])
def createDireccion():
    return cntCreateDireccion()


@dir_bp.route('/', methods=['PUT'])
def updateDireccion():
    return cntUpdateDireccion()


@dir_bp.route('/', methods=['DELETE'])
def deleteDireccion():
    return cntDeleteDireccion()


@dir_bp.route('/user/<user_id>', methods=['GET'])
def listDireccionesByUser(user_id):
    return cntListDireccionesByUser(user_id)


# http://128.9.9.9/direcciones/
# http://128.9.9.9/direcciones/            (POST -> crear)
# http://128.9.9.9/direcciones/            (PUT  -> editar)
# http://128.9.9.9/direcciones/            (DELETE -> eliminar)
# http://128.9.9.9/direcciones/user/3