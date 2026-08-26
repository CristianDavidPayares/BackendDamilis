from flask import Blueprint
from Controllers.Insumo_controller import (
    cntListInsumos,
    cntCreateInsumo,
    cntUpdateInsumo,
    cntDeleteInsumo,
    cntSearchByCodigo,
    cntListInsumosByTipo
)

ins_bp = Blueprint('insumo_bp', __name__)


@ins_bp.route('/', methods=['GET'])
def listInsumos():
    return cntListInsumos()


@ins_bp.route('/', methods=['POST'])
def createInsumo():
    return cntCreateInsumo()


@ins_bp.route('/', methods=['PUT'])
def updateInsumo():
    return cntUpdateInsumo()


@ins_bp.route('/', methods=['DELETE'])
def deleteInsumo():
    return cntDeleteInsumo()


@ins_bp.route('/search/<codigo>', methods=['GET'])
def searchInsumoByCodigo(codigo):
    return cntSearchByCodigo(codigo)


@ins_bp.route('/tipo/<tipo_insumo>', methods=['GET'])
def listInsumosByTipo(tipo_insumo):
    return cntListInsumosByTipo(tipo_insumo)


# http://128.9.9.9/insumos/
# http://128.9.9.9/insumos/            (POST -> crear)
# http://128.9.9.9/insumos/            (PUT  -> editar)
# http://128.9.9.9/insumos/            (DELETE -> eliminar)
# http://128.9.9.9/insumos/search/COD001
# http://128.9.9.9/insumos/tipo/tela