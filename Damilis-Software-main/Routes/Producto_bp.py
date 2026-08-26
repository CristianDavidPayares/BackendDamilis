from flask import Blueprint
from Controllers.Producto_controller import (
    cntListProductos,
    cntCreateProducto,
    cntUpdateProducto,
    cntDeleteProducto,
    cntSearchByCodigo,
    cntUpdateCantidad
)

pro_bp = Blueprint('producto_bp', __name__)


@pro_bp.route('/', methods=['GET'])
def listProductos():
    return cntListProductos()


@pro_bp.route('/', methods=['POST'])
def createProducto():
    return cntCreateProducto()


@pro_bp.route('/', methods=['PUT'])
def updateProducto():
    return cntUpdateProducto()


@pro_bp.route('/', methods=['DELETE'])
def deleteProducto():
    return cntDeleteProducto()


@pro_bp.route('/search/<codigo>', methods=['GET'])
def searchProductoByCodigo(codigo):
    return cntSearchByCodigo(codigo)


@pro_bp.route('/cantidad', methods=['PUT'])
def updateCantidadProducto():
    return cntUpdateCantidad()


# http://128.9.9.9/productos/
# http://128.9.9.9/productos/          (POST -> crear)
# http://128.9.9.9/productos/          (PUT  -> editar)
# http://128.9.9.9/productos/          (DELETE -> eliminar)
# http://128.9.9.9/productos/search/ABC123
# http://128.9.9.9/productos/cantidad  (PUT -> actualizar solo stock)