from flask import jsonify, request
from Services.Admin_services import (
    servListAdmin,
    addAdmin,
    upAdmin,
    delAdmin,
    searchByUserId
)


class AdminController:

    # Listar todos los administradores
    def ListAdmins():
        data = servListAdmin()
        return jsonify(data), 200

    # Crear un administrador
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        user_id = body.get("user_id")
        actual_catalogo = body.get("actual_catalogo")
        observaciones = body.get("observaciones")

        if not user_id:
            return jsonify({
                "error": "user_id es obligatorio"
            }), 400

        if searchByUserId(user_id) is not None:
            return jsonify({
                "error": "Este usuario ya tiene un perfil de administrador"
            }), 409

        nuevo_admin = addAdmin(
            actual_catalogo,
            observaciones,
            user_id
        )

        return jsonify(nuevo_admin), 201

    # Actualizar un administrador
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        actual_catalogo = body.get("actual_catalogo")
        observaciones = body.get("observaciones")

        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = upAdmin(
            id,
            actual_catalogo,
            observaciones
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Administrador no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Administrador actualizado correctamente"
        }), 200

    # Eliminar un administrador
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delAdmin(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Administrador no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Administrador eliminado correctamente"
        }), 200

    # Buscar administrador por ID de usuario
    def SearchByUserId(user_id):
        admin = searchByUserId(user_id)

        if admin is None:
            return jsonify({
                "error": "Administrador no encontrado"
            }), 404

        return jsonify(admin), 200