from flask import jsonify, request
from Services.Cliente_services import (
    servListCliente,
    addCliente,
    upCliente,
    delCliente,
    cambiarEstado,
    searchByCedula,
    searchByUserId
)


class ClienteController:

    # Listar todos los clientes
    def ListClientes():
        data = servListCliente()
        return jsonify(data), 200

    # Crear un cliente
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        preferencias = body.get("preferencias")
        per_cedula = body.get("per_cedula")
        user_id = body.get("user_id")

        if not per_cedula or not user_id:
            return jsonify({
                "error": "per_cedula y user_id son obligatorios"
            }), 400

        if searchByCedula(per_cedula) is not None:
            return jsonify({
                "error": "Ya existe un cliente con esa cédula"
            }), 409

        nuevo_cliente = addCliente(
            preferencias,
            per_cedula,
            user_id
        )

        return jsonify(nuevo_cliente), 201

    # Actualizar un cliente
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        preferencias = body.get("preferencias")

        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = upCliente(
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
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delCliente(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Cliente eliminado correctamente"
        }), 200

    # Cambiar estado de un cliente
    def CambiarEstado():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        estado = body.get("estado")

        if not id or not estado:
            return jsonify({
                "error": "id y estado son obligatorios"
            }), 400

        filas_afectadas = cambiarEstado(
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
    def SearchByCedula(per_cedula):
        cliente = searchByCedula(per_cedula)

        if cliente is None:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify(cliente), 200

    # Buscar cliente por ID de usuario
    def SearchByUserId(user_id):
        cliente = searchByUserId(user_id)

        if cliente is None:
            return jsonify({
                "error": "Cliente no encontrado"
            }), 404

        return jsonify(cliente), 200