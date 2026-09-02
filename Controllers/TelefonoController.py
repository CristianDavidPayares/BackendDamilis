from flask import jsonify, request
from Services.TelefonoService import TelefonoService


class TelefonoController:
    
    def listar():
        data = TelefonoService.listar()
        return jsonify(data), 200


    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        user_id = body.get("user_id")
        telefono = body.get("telefono")

        if user_id is None or telefono is None:
            return jsonify({
                "error": "user_id y telefono son obligatorios"
            }), 400

        # Validar user_id (entero positivo)
        try:
            user_id = int(user_id)
            if user_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "user_id debe ser un entero positivo"
            }), 400

        # Validar teléfono (string no vacío)
        if not isinstance(telefono, str) or not telefono.strip():
            return jsonify({
                "error": "telefono debe ser una cadena de texto válida"
            }), 400

        telefono = telefono.strip()

        nuevo_telefono = TelefonoService.crear(user_id, telefono)
        return jsonify(nuevo_telefono), 201


    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        telefono = body.get("telefono")

        if id is None or telefono is None:
            return jsonify({
                "error": "id y telefono son obligatorios"
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

        # Validar teléfono (string no vacío)
        if not isinstance(telefono, str) or not telefono.strip():
            return jsonify({
                "error": "telefono debe ser una cadena de texto válida"
            }), 400

        telefono = telefono.strip()

        filas_afectadas = TelefonoService.actualizar(id, telefono)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Teléfono no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Teléfono actualizado correctamente"
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

        filas_afectadas = TelefonoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Teléfono no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Teléfono eliminado correctamente"
        }), 200


    def listarPorUsuario(user_id):
        if user_id is None:
            return jsonify({
                "error": "user_id es obligatorio"
            }), 400

        try:
            user_id = int(user_id)
            if user_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "user_id debe ser un entero positivo"
            }), 400

        data = TelefonoService.listarPorUsuario(user_id)
        return jsonify(data), 200