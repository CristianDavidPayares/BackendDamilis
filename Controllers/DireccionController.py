from flask import jsonify, request
from Services.DireccionService import DireccionService

class DireccionController:

    
    def listar():
        data = DireccionService.listar()
        return jsonify(data), 200

    
    def crear():
        body = request.get_json(silent=True)
        if not body:
            return jsonify({"error": "El cuerpo de la petición es obligatorio"}), 400
        user_id = body.get("user_id")
        direccion = body.get("direccion")
        if user_id is None or direccion is None:
            return jsonify({"error": "user_id y direccion son obligatorios"}), 400
        # Validar user_id entero positivo
        try:
            user_id = int(user_id)
            if user_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "user_id debe ser un entero positivo"}), 400
        # Validar direccion string no vacío
        if not isinstance(direccion, str) or not direccion.strip():
            return jsonify({"error": "direccion debe ser una cadena de texto válida"}), 400
        direccion = direccion.strip()
        nueva_direccion = DireccionService.crear(user_id, direccion)
        return jsonify(nueva_direccion), 201

    
    def actualizar():
        body = request.get_json(silent=True)
        if not body:
            return jsonify({"error": "El cuerpo de la petición es obligatorio"}), 400
        id = body.get("id")
        direccion = body.get("direccion")
        if id is None or direccion is None:
            return jsonify({"error": "id y direccion son obligatorios"}), 400
        try:
            id = int(id)
            if id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "id debe ser un entero positivo"}), 400
        if not isinstance(direccion, str) or not direccion.strip():
            return jsonify({"error": "direccion debe ser una cadena de texto válida"}), 400
        direccion = direccion.strip()
        filas_afectadas = DireccionService.actualizar(id, direccion)
        if filas_afectadas == 0:
            return jsonify({"error": "Dirección no encontrada"}), 404
        return jsonify({"mensaje": "Dirección actualizada correctamente"}), 200

    
    def eliminar(id):
        if id is None:
            return jsonify({"error": "id es obligatorio"}), 400
        try:
            id = int(id)
            if id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "id debe ser un entero positivo"}), 400
        filas_afectadas = DireccionService.eliminar(id)
        if filas_afectadas == 0:
            return jsonify({"error": "Dirección no encontrada"}), 404
        return jsonify({"mensaje": "Dirección eliminada correctamente"}), 200

    
    def listarPorUsuario(user_id):
        if user_id is None:
            return jsonify({"error": "user_id es obligatorio"}), 400
        try:
            user_id = int(user_id)
            if user_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "user_id debe ser un entero positivo"}), 400
        data = DireccionService.listarPorUsuario(user_id)
        return jsonify(data), 200