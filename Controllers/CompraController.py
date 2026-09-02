from flask import jsonify, request
from Services.CompraService import CompraService


class CompraController:

    # Listar todas las compras
    def listar():
        data = CompraService.listar()
        return jsonify(data), 200


    # Crear una compra
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        subtotal = body.get("subtotal")
        metodo_pago = body.get("metodo_pago")
        numero_compras = body.get("numero_compras")
        cli_id = body.get("cli_id")

        # Validar campos obligatorios
        if subtotal is None or metodo_pago is None or cli_id is None:
            return jsonify({
                "error": "subtotal, metodo_pago y cli_id son obligatorios"
            }), 400

        # Validar subtotal
        try:
            subtotal = float(subtotal)

            if subtotal < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "subtotal debe ser un número mayor o igual a 0"
            }), 400

        # Validar método de pago
        if not isinstance(metodo_pago, str) or not metodo_pago.strip():
            return jsonify({
                "error": "metodo_pago debe ser una cadena de texto válida"
            }), 400

        metodo_pago = metodo_pago.strip()

        # Validar número de compras
        if numero_compras is None:
            return jsonify({
                "error": "numero_compras es obligatorio"
            }), 400

        try:
            numero_compras = int(numero_compras)

            if numero_compras < 1:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "numero_compras debe ser un entero mayor o igual a 1"
            }), 400

        # Validar ID del cliente
        try:
            cli_id = int(cli_id)

            if cli_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cli_id debe ser un entero positivo"
            }), 400

        nueva_compra = CompraService.crear(
            subtotal,
            metodo_pago,
            numero_compras,
            cli_id
        )

        return jsonify(nueva_compra), 201


    # Actualizar una compra
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        subtotal = body.get("subtotal")
        metodo_pago = body.get("metodo_pago")
        numero_compras = body.get("numero_compras")

        # Validar ID
        if id is None:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        try:
            id = int(id)

            if id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        # Validar subtotal
        if subtotal is None:
            return jsonify({
                "error": "subtotal es obligatorio"
            }), 400

        try:
            subtotal = float(subtotal)

            if subtotal < 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "subtotal debe ser un número mayor o igual a 0"
            }), 400

        # Validar método de pago
        if metodo_pago is None:
            return jsonify({
                "error": "metodo_pago es obligatorio"
            }), 400

        if not isinstance(metodo_pago, str) or not metodo_pago.strip():
            return jsonify({
                "error": "metodo_pago debe ser una cadena de texto válida"
            }), 400

        metodo_pago = metodo_pago.strip()

        # Validar número de compras
        if numero_compras is None:
            return jsonify({
                "error": "numero_compras es obligatorio"
            }), 400

        try:
            numero_compras = int(numero_compras)

            if numero_compras < 1:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "numero_compras debe ser un entero mayor o igual a 1"
            }), 400

        filas_afectadas = CompraService.actualizar(
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
    def eliminar(id):
        if id is None:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        try:
            id = int(id)

            if id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        filas_afectadas = CompraService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Compra no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Compra eliminada correctamente"
        }), 200


    # Listar compras de un cliente
    def listarPorCliente(cli_id):
        if cli_id is None:
            return jsonify({
                "error": "cli_id es obligatorio"
            }), 400

        try:
            cli_id = int(cli_id)

            if cli_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "cli_id debe ser un entero positivo"
            }), 400

        data = CompraService.listarPorCliente(cli_id)

        return jsonify(data), 200