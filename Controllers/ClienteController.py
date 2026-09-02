from flask import jsonify, request
from Services.ClienteService import ClienteService


class ClienteController:

    # Listar todos los clientes
    def listar():
        data = ClienteService.listar()
        return jsonify(data), 200


    # Crear un cliente
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        preferencias = body.get("preferencias")
        per_cedula = body.get("per_cedula")
        user_id = body.get("user_id")

        # Validar campos obligatorios
        if not per_cedula or user_id is None:
            return jsonify({
                "error": "per_cedula y user_id son obligatorios"
            }), 400

        # Validar cédula
        per_cedula_str = str(per_cedula).strip()

        if not per_cedula_str.isdigit():
            return jsonify({
                "error": "per_cedula debe ser un número de identificación válido"
            }), 400

        # Validar user_id
        try:
            user_id = int(user_id)

            if user_id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "user_id debe ser un entero positivo"
            }), 400

        # Validar preferencias
        if preferencias is not None and not isinstance(preferencias, str):
            return jsonify({
                "error": "preferencias debe ser una cadena de texto"
            }), 400

        # Verificar que no exista otro cliente con esa cédula
        if ClienteService.buscarPorCedula(per_cedula_str) is not None:
            return jsonify({
                "error": "Ya existe un cliente con esa cédula"
            }), 409

        nuevo_cliente = ClienteService.crear(
            preferencias,
            per_cedula_str,
            user_id
        )

        return jsonify(nuevo_cliente), 201


    # Actualizar un cliente
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        preferencias = body.get("preferencias")

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

        # Validar preferencias
        if preferencias is not None and not isinstance(preferencias, str):
            return jsonify({
                "error": "preferencias debe ser una cadena de texto"
            }), 400

        filas_afectadas = ClienteService.actualizar(
            id,
            preferencias
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Cliente actualizado correctamente"
        }), 200


    # Eliminar un cliente
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

        filas_afectadas = ClienteService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Cliente eliminado correctamente"
        }), 200


    # Cambiar estado de un cliente
    def cambiarEstado():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        estado = body.get("estado")

        if id is None or not estado:
            return jsonify({
                "error": "id y estado son obligatorios"
            }), 400

        # Validar ID
        try:
            id = int(id)

            if id <= 0:
                raise ValueError

        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        # Validar estado
        if not isinstance(estado, str) or estado.strip().upper() not in [
            "ACTIVO",
            "INACTIVO"
        ]:
            return jsonify({
                "error": "El estado debe ser 'ACTIVO' o 'INACTIVO'"
            }), 400

        estado = estado.strip().upper()

        filas_afectadas = ClienteService.cambiarEstado(
            id,
            estado
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Estado actualizado correctamente"
        }), 200


    # Buscar cliente por cédula
    def buscarPorCedula(per_cedula):

        if not per_cedula or not str(per_cedula).strip().isdigit():
            return jsonify({
                "error": "per_cedula debe ser un número de identificación válido"
            }), 400

        per_cedula = str(per_cedula).strip()

        cliente = ClienteService.buscarPorCedula(per_cedula)

        if cliente is None:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify(cliente), 200


    # Buscar cliente por ID de usuario
    def buscarPorUserId(user_id):

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

        cliente = ClienteService.buscarPorUserId(user_id)

        if cliente is None:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify(cliente), 200