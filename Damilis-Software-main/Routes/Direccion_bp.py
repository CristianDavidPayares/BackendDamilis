from flask import Blueprint
<<<<<<< Updated upstream
from Controllers.Direccion_controller import (
    cntListDirecciones,
    cntCreateDireccion,
    cntUpdateDireccion,
    cntDeleteDireccion,
    cntListDireccionesByUser
)
=======
from Controllers.Direccion_controller import DireccionController
>>>>>>> Stashed changes

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


<<<<<<< Updated upstream
@dir_bp.route('/', methods=['DELETE'])
def deleteDireccion():
    return cntDeleteDireccion()
=======
@dir_bp.route('/<id>', methods=['DELETE'])
def deleteDireccion(id):
    return DireccionController.delete(id)
>>>>>>> Stashed changes


@dir_bp.route('/user/<user_id>', methods=['GET'])
def listDireccionesByUser(user_id):
    return cntListDireccionesByUser(user_id)


# http://128.9.9.9/direcciones/
# http://128.9.9.9/direcciones/            (POST -> crear)
# http://128.9.9.9/direcciones/            (PUT  -> editar)
# http://128.9.9.9/direcciones/<id>        (DELETE -> eliminar)
# http://128.9.9.9/direcciones/user/3