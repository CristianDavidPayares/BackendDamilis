from flask import jsonify, request
from Services.Producto_services import (
    servListProducto,
    addProducto,
    upProducto,
    delProducto,
    searchByCodigo,
    updateCantidad
)


class ProductoController:

    # Listar todos los productos
    def ListProductos():
        data = servListProducto()
        return jsonify(data), 200

    # Crear un producto
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        codigo = body.get("codigo")
        talla = body.get("talla")
        color = body.get("color")
        resena = body.get("resena")
        descripcion = body.get("descripcion")
        precio = body.get("precio")
        calificacion = body.get("calificacion")
        imagen = body.get("imagen")
        cantidad = body.get("cantidad")

        if not codigo or precio is None or cantidad is None:
            return jsonify({
                "error": "codigo, precio y cantidad son obligatorios"
            }), 400

        if searchByCodigo(codigo) is not None:
            return jsonify({
                "error": "Ya existe un producto con ese código"
            }), 409

        nuevo_producto = addProducto(
            codigo,
            talla,
            color,
            resena,
            descripcion,
            precio,
            calificacion,
            imagen,
            cantidad
        )

        return jsonify(nuevo_producto), 201

    # Actualizar un producto
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        codigo = body.get("codigo")
        talla = body.get("talla")
        color = body.get("color")
        resena = body.get("resena")
        descripcion = body.get("descripcion")
        precio = body.get("precio")
        calificacion = body.get("calificacion")
        imagen = body.get("imagen")
        cantidad = body.get("cantidad")

        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = upProducto(
            id,
            codigo,
            talla,
            color,
            resena,
            descripcion,
            precio,
            calificacion,
            imagen,
            cantidad
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Producto actualizado correctamente"
        }), 200

    # Eliminar un producto
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delProducto(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Producto eliminado correctamente"
        }), 200

    # Buscar producto por código
    def SearchByCodigo(codigo):
        producto = searchByCodigo(codigo)

        if producto is None:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify(producto), 200

    # Actualizar cantidad de un producto
    def UpdateCantidad():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        cantidad = body.get("cantidad")

        if not id or cantidad is None:
            return jsonify({
                "error": "id y cantidad son obligatorios"
            }), 400

        filas_afectadas = updateCantidad(
            id,
            cantidad
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Cantidad actualizada correctamente"
        }), 200