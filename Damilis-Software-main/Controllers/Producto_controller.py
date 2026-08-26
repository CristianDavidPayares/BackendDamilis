from flask import jsonify, request
from Services.Producto_services import (
    servListProducto,
    addProducto,
    upProducto,
    delProducto,
    searchByCodigo,
    updateCantidad
)


def cntListProductos():
    data = servListProducto()
    return jsonify(data), 200


def cntCreateProducto():
    body = request.get_json()

    codigo          = body.get("codigo")
    talla           = body.get("talla")
    color           = body.get("color")
    resena          = body.get("resena")
    descripcion     = body.get("descripcion")
    precio          = body.get("precio")
    calificacion    = body.get("calificacion")
    imagen          = body.get("imagen")
    cantidad        = body.get("cantidad")

    if not codigo or precio is None or cantidad is None:
        return jsonify({"error": "codigo, precio y cantidad son obligatorios"}), 400

    nuevo_producto = addProducto(codigo, talla, color, resena, descripcion, precio, calificacion, imagen, cantidad)
    return jsonify(nuevo_producto), 201


def cntUpdateProducto():
    body = request.get_json()

    id              = body.get("id")
    codigo          = body.get("codigo")
    talla           = body.get("talla")
    color           = body.get("color")
    resena          = body.get("resena")
    descripcion     = body.get("descripcion")
    precio          = body.get("precio")
    calificacion    = body.get("calificacion")
    imagen          = body.get("imagen")
    cantidad        = body.get("cantidad")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = upProducto(id, codigo, talla, color, resena, descripcion, precio, calificacion, imagen, cantidad)

    if filas_afectadas == 0:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto actualizado correctamente"}), 200


def cntDeleteProducto():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delProducto(id)

    if filas_afectadas == 0:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto eliminado correctamente"}), 200


def cntSearchByCodigo(codigo):
    producto = searchByCodigo(codigo)

    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify(producto), 200


def cntUpdateCantidad():
    body = request.get_json()

    id          = body.get("id")
    cantidad    = body.get("cantidad")

    if not id or cantidad is None:
        return jsonify({"error": "id y cantidad son obligatorios"}), 400

    filas_afectadas = updateCantidad(id, cantidad)

    if filas_afectadas == 0:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Cantidad actualizada correctamente"}), 200