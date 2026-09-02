from flask import jsonify, request
from Services.PqrService import PqrService


class PqrController:

    def listar():
        data = PqrService.listar()
        return jsonify(data), 200


    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        descripcion = body.get("descripcion")
        cli_id = body.get("cli_id")

        if descripcion is None or cli_id is None:
            return jsonify({
                "error": "descripcion y cli_id son obligatorios"
            }), 400

        # Validar descripcion (string no vacío)
        if not isinstance(descripcion, str) or not descripcion.strip():
            return jsonify({
                "error": "descripcion debe ser una cadena de texto válida"
            }), 400
        descripcion = descripcion.strip()

        # Validar cli_id (entero positivo)
        try:
            cli_id = int(cli_id)
            if cli_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "cli_id debe ser un entero positivo"
            }), 400

        nueva_pqr = PqrService.crear(descripcion, cli_id)
        return jsonify(nueva_pqr), 201


    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        descripcion = body.get("descripcion")

        if id is None or descripcion is None:
            return jsonify({
                "error": "id y descripcion son obligatorios"
            }), 400

        # Validar id (entero positivo)
        try:
            id = int(id)
            if id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        # Validar descripcion (string no vacío)
        if not isinstance(descripcion, str) or not descripcion.strip():
            return jsonify({
                "error": "descripcion debe ser una cadena de texto válida"
            }), 400
        descripcion = descripcion.strip()

        filas_afectadas = PqrService.actualizar(id, descripcion)

        if filas_afectadas == 0:
            return jsonify({
                "error": "PQR no encontrada"
            }), 404

        return jsonify({
            "mensaje": "PQR actualizada correctamente"
        }), 200


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

        filas_afectadas = PqrService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "PQR no encontrada"
            }), 404

        return jsonify({
            "mensaje": "PQR eliminada correctamente"
        }), 200


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

        data = PqrService.listarPorCliente(cli_id)
        return jsonify(data), 200


    def responder():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        estado = body.get("estado")

        if id is None or estado is None:
            return jsonify({
                "error": "id y estado son obligatorios"
            }), 400

        # Validar id (entero positivo)
        try:
            id = int(id)
            if id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        # Validar estado (string no vacío)
        if not isinstance(estado, str) or not estado.strip():
            return jsonify({
                "error": "estado debe ser una cadena de texto válida"
            }), 400
        estado = estado.strip()

        filas_afectadas = PqrService.responder(id, estado)

        if filas_afectadas == 0:
            return jsonify({
                "error": "PQR no encontrada"
            }), 404

        return jsonify({
            "mensaje": "PQR respondida correctamente"
        }), 200