from flask import jsonify, request
from Services.Telefono_services import (
    servListTelefono,
    addTelefono,
    upTelefono,
    delTelefono,
    servListTelefonoByUser
)


class TelefonoController:

    # Listar todos los teléfonos
    def ListTelefonos():
        data = servListTelefono()
        return jsonify(data), 200

    # Crear un teléfono
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        user_id = body.get("user_id")
        telefono = body.get("telefono")

        if not user_id or not telefono:
            return jsonify({
                "error": "user_id y telefono son obligatorios"
            }), 400

        nuevo_telefono = addTelefono(
            user_id,
            telefono
        )

        return jsonify(nuevo_telefono), 201

    # Actualizar un teléfono
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        telefono = body.get("telefono")

        if not id or not telefono:
            return jsonify({
                "error": "id y telefono son obligatorios"
            }), 400

        filas_afectadas = upTelefono(
            id,
            telefono
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Teléfono no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Teléfono actualizado correctamente"
        }), 200

    # Eliminar un teléfono
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delTelefono(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Teléfono no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Teléfono eliminado correctamente"
        }), 200

    # Listar teléfonos por usuario
    def ListTelefonosByUser(user_id):
        data = servListTelefonoByUser(user_id)
        return jsonify(data), 200