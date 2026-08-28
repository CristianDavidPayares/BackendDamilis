from flask import Blueprint
from Controllers.Categoria_controller import CategoriaController


cat_bp = Blueprint('categoria_bp', __name__)


# Listar todas las categorías
@cat_bp.route('/', methods=['GET'])
def listCategorias():
    return CategoriaController.ListCategorias()


# Buscar categoría por tipo
@cat_bp.route('/tipo/<tipo_categoria>', methods=['GET'])
def searchCategoriaByTipo(tipo_categoria):
    return CategoriaController.SearchByTipo(tipo_categoria)


# Crear una categoría
@cat_bp.route('/', methods=['POST'])
def createCategoria():
    return CategoriaController.create()


# Actualizar una categoría
@cat_bp.route('/', methods=['PUT'])
def updateCategoria():
    return CategoriaController.update()


# Eliminar una categoría
@cat_bp.route('/<int:id>', methods=['DELETE'])
def deleteCategoria(id):
    return CategoriaController.delete(id)


# http://128.9.9.9/categorias/
# http://128.9.9.9/categorias/         (POST -> crear)
# http://128.9.9.9/categorias/         (PUT  -> editar)
# http://128.9.9.9/categorias/         (DELETE -> eliminar)