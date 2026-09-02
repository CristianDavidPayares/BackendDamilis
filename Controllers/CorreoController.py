from flask import jsonify, request
from Services.CorreoService import CorreoService


class CorreoController:

    # Listar todos los correos
    def listar():
        data = CorreoService.listar()
        return jsonify(data), 200


    # Crear un correo
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        user_id = body.get("user_id")
        correo = body.get("correo")

        # Validar campos obligatorios
        if user_id is None or correo is None:
            return jsonify({
                "error": "user_id y correo son obligatorios"
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

        # Validar correo (string no vacío)
        if not isinstance(correo, str) or not correo.strip():
            return jsonify({
                "error": "correo debe ser una cadena de texto válida"
            }), 400

        correo = correo.strip()

        # Verificar si el correo ya existe
        if CorreoService.buscarPorCorreo(correo) is not None:
            return jsonify({
                "error": "El correo ya está registrado"
            }), 409

        nuevo_correo = CorreoService.crear(user_id, correo)
        return jsonify(nuevo_correo), 201


    # Actualizar un correo
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        correo = body.get("correo")

        if id is None or correo is None:
            return jsonify({
                "error": "id y correo son obligatorios"
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

        # Validar correo (string no vacío)
        if not isinstance(correo, str) or not correo.strip():
            return jsonify({
                "error": "correo debe ser una cadena de texto válida"
            }), 400

        correo = correo.strip()

        filas_afectadas = CorreoService.actualizar(id, correo)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Correo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Correo actualizado correctamente"
        }), 200


    # Eliminar un correo
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

        filas_afectadas = CorreoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Correo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Correo eliminado correctamente"
        }), 200


    # Listar correos por usuario
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

        data = CorreoService.listarPorUsuario(user_id)
        return jsonify(data), 200


    # Buscar un correo por su dirección
    def buscarPorCorreo(correo):
        if correo is None:
            return jsonify({
                "error": "correo es obligatorio"
            }), 400

        if not isinstance(correo, str) or not correo.strip():
            return jsonify({
                "error": "correo debe ser una cadena de texto válida"
            }), 400

        correo = correo.strip()
        resultado = CorreoService.buscarPorCorreo(correo)

        if resultado is None:
            return jsonify({
                "error": "Correo no encontrado"
            }), 404

        return jsonify(resultado), 200