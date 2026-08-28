from flask import jsonify, request
from Services.Compra_services import (
    servListCompra,
    addCompra,
    upCompra,
    delCompra,
    servListCompraByCliente
)


class CompraController:

    # Listar todas las compras
    def ListCompras():
        data = servListCompra()
        return jsonify(data), 200

    # Crear una compra
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        subtotal = body.get("subtotal")
        metodo_pago = body.get("metodo_pago")
        numero_compras = body.get("numero_compras")
        cli_id = body.get("cli_id")

        if subtotal is None or not metodo_pago or not cli_id:
            return jsonify({
                "error": "subtotal, metodo_pago y cli_id son obligatorios"
            }), 400

        nueva_compra = addCompra(
            subtotal,
            metodo_pago,
            numero_compras,
            cli_id
        )

        return jsonify(nueva_compra), 201

    # Actualizar una compra
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        subtotal = body.get("subtotal")
        metodo_pago = body.get("metodo_pago")
        numero_compras = body.get("numero_compras")

        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = upCompra(
            id,
            subtotal,
            metodo_pago,
            numero_compras
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Compra no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Compra actualizada correctamente"
        }), 200

    # Eliminar una compra
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delCompra(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Compra no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Compra eliminada correctamente"
        }), 200

    # Listar compras de un cliente
    def ListComprasByCliente(cli_id):
        data = servListCompraByCliente(cli_id)
        return jsonify(data), 200