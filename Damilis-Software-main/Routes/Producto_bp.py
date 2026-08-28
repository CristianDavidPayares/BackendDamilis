from flask import Blueprint
from Controllers.Producto_controller import ProductoController


prod_bp = Blueprint('producto_bp', __name__)


# Listar todos los productos
@prod_bp.route('/', methods=['GET'])
def listProductos():
    return ProductoController.ListProductos()


# Crear un producto
@prod_bp.route('/', methods=['POST'])
def createProducto():
    return ProductoController.create()


# Actualizar un producto
@prod_bp.route('/', methods=['PUT'])
def updateProducto():
    return ProductoController.update()


# Eliminar un producto
@prod_bp.route('/<int:id>', methods=['DELETE'])
def deleteProducto(id):
    return ProductoController.delete(id)


# Buscar producto por código
@prod_bp.route('/codigo/<codigo>', methods=['GET'])
def searchProductoByCodigo(codigo):
    return ProductoController.SearchByCodigo(codigo)


# Actualizar cantidad de un producto
@prod_bp.route('/cantidad', methods=['PUT'])
def updateCantidad():
    return ProductoController.UpdateCantidad()


# http://128.9.9.9/productos/
# http://128.9.9.9/productos/          (POST -> crear)
# http://128.9.9.9/productos/          (PUT  -> editar)
# http://128.9.9.9/productos/          (DELETE -> eliminar)
# http://128.9.9.9/productos/search/ABC123
# http://128.9.9.9/productos/cantidad  (PUT -> actualizar solo stock)