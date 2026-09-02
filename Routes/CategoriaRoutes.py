from flask import Blueprint
from Controllers.CategoriaController import CategoriaController


cat_bp = Blueprint('categoria_bp', __name__)


# Listar todas las categorías
@cat_bp.route('/', methods=['GET'])
def listCategorias():
    return CategoriaController.listar()


# Buscar categoría por tipo
@cat_bp.route('/tipo/<tipo_categoria>', methods=['GET'])
def searchCategoriaByTipo(tipo_categoria):
    return CategoriaController.buscarPorTipo(tipo_categoria)


# Crear una categoría
@cat_bp.route('/', methods=['POST'])
def createCategoria():
    return CategoriaController.crear()


# Actualizar una categoría
@cat_bp.route('/', methods=['PUT'])
def updateCategoria():
    return CategoriaController.actualizar()


# Eliminar una categoría
@cat_bp.route('/<int:id>', methods=['DELETE'])
def deleteCategoria(id):
    return CategoriaController.eliminar(id)