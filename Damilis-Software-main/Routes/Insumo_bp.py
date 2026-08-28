from flask import Blueprint
from Controllers.Insumo_controller import InsumoController


ins_bp = Blueprint('insumo_bp', __name__)


# Listar todos los insumos
@ins_bp.route('/', methods=['GET'])
def listInsumos():
    return InsumoController.ListInsumos()


# Crear un insumo
@ins_bp.route('/', methods=['POST'])
def createInsumo():
    return InsumoController.create()


# Actualizar un insumo
@ins_bp.route('/', methods=['PUT'])
def updateInsumo():
    return InsumoController.update()


# Eliminar un insumo
@ins_bp.route('/<int:id>', methods=['DELETE'])
def deleteInsumo(id):
    return InsumoController.delete(id)


# Buscar insumo por código
@ins_bp.route('/codigo/<codigo>', methods=['GET'])
def searchInsumoByCodigo(codigo):
    return InsumoController.SearchByCodigo(codigo)


# Listar insumos por tipo
@ins_bp.route('/tipo/<tipo_insumo>', methods=['GET'])
def listInsumosByTipo(tipo_insumo):
    return InsumoController.ListInsumosByTipo(tipo_insumo)

# http://128.9.9.9/insumos/
# http://128.9.9.9/insumos/            (POST -> crear)
# http://128.9.9.9/insumos/            (PUT  -> editar)
# http://128.9.9.9/insumos/            (DELETE -> eliminar)
# http://128.9.9.9/insumos/search/COD001
# http://128.9.9.9/insumos/tipo/tela