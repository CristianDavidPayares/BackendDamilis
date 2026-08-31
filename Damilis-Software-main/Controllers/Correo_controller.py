import re
from flask import jsonify, request
from Services.Correo_services import (
    servListCorreo,
    addCorreo,
    upCorreo,
    delCorreo,
    servListCorreoByUser,
    searchByCorreo
)

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def cntListCorreos():
    data = servListCorreo()
    return jsonify(data), 200


def cntCreateCorreo():
    body = request.get_json()

    user_id = body.get("user_id")
    correo  = body.get("correo")

    if not user_id or not correo:
        return jsonify({"error": "user_id y correo son obligatorios"}), 400

<<<<<<< Updated upstream
    if searchByCorreo(correo) is not None:
        return jsonify({"error": "El correo ya está registrado"}), 409

    nuevo_correo = addCorreo(user_id, correo)
    return jsonify(nuevo_correo), 201


def cntUpdateCorreo():
    body = request.get_json()
=======
        if user_id is None or not correo:
            return jsonify({
                "error": "user_id y correo son obligatorios"
            }), 400

        try:
            user_id = int(user_id)
            if user_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "user_id debe ser un entero positivo"
            }), 400

        if not isinstance(correo, str) or not correo.strip():
            return jsonify({
                "error": "correo debe ser una cadena de texto válida"
            }), 400
        correo = correo.strip().lower()

        if not EMAIL_REGEX.match(correo):
            return jsonify({
                "error": "correo no tiene un formato de email válido"
            }), 400

        if searchByCorreo(correo) is not None:
            return jsonify({
                "error": "El correo ya está registrado"
            }), 409

        nuevo_correo = addCorreo(user_id, correo)
        return jsonify(nuevo_correo), 201
>>>>>>> Stashed changes

    id      = body.get("id")
    correo  = body.get("correo")

    if not id or not correo:
        return jsonify({"error": "id y correo son obligatorios"}), 400

    filas_afectadas = upCorreo(id, correo)

<<<<<<< Updated upstream
    if filas_afectadas == 0:
        return jsonify({"error": "Correo no encontrado"}), 404

    return jsonify({"mensaje": "Correo actualizado correctamente"}), 200
=======
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

        if correo is not None:
            if not isinstance(correo, str) or not correo.strip():
                return jsonify({
                    "error": "correo debe ser una cadena de texto válida"
                }), 400
            correo = correo.strip().lower()

            if not EMAIL_REGEX.match(correo):
                return jsonify({
                    "error": "correo no tiene un formato de email válido"
                }), 400

            existente = searchByCorreo(correo)
            if existente is not None and existente.get("id") != id:
                return jsonify({
                    "error": "El correo ya está registrado por otro usuario"
                }), 409
        else:
            return jsonify({
                "error": "correo es obligatorio para actualizar"
            }), 400

        filas_afectadas = upCorreo(id, correo)
>>>>>>> Stashed changes


def cntDeleteCorreo():
    body = request.get_json()
    id = body.get("id")

<<<<<<< Updated upstream
    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delCorreo(id)
=======
    # Eliminar un correo
    def delete(id):
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

        filas_afectadas = delCorreo(id)
>>>>>>> Stashed changes

    if filas_afectadas == 0:
        return jsonify({"error": "Correo no encontrado"}), 404

    return jsonify({"mensaje": "Correo eliminado correctamente"}), 200

<<<<<<< Updated upstream

def cntListCorreosByUser(user_id):
    data = servListCorreoByUser(user_id)
    return jsonify(data), 200
=======
    # Listar correos de un usuario
    def ListCorreosByUser(user_id):
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

        data = servListCorreoByUser(user_id)
        return jsonify(data), 200
>>>>>>> Stashed changes
