from flask import Blueprint
from Controllers.Categoria_controller import (
    cntListCategorias,
    cntCreateCategoria,
    cntUpdateCategoria,
    cntDeleteCategoria
)

cat_bp = Blueprint('categoria_bp', __name__)


@cat_bp.route('/', methods=['GET'])
def listCategorias():
    return cntListCategorias()


@cat_bp.route('/', methods=['POST'])
def createCategoria():
    return cntCreateCategoria()


@cat_bp.route('/', methods=['PUT'])
def updateCategoria():
    return cntUpdateCategoria()


@cat_bp.route('/<int:id>', methods=['DELETE'])
def deleteCategoria(id):
    return cntDeleteCategoria(id)


# http://128.9.9.9/categorias/
# http://128.9.9.9/categorias/         (POST -> crear)
# http://128.9.9.9/categorias/         (PUT  -> editar)
# http://128.9.9.9/categorias/         (DELETE -> eliminar)