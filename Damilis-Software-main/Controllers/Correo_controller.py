from flask import jsonify, request
from Services.Correo_services import (
    servListCorreo,
    addCorreo,
    upCorreo,
    delCorreo,
    servListCorreoByUser,
    searchByCorreo
)


def cntListCorreos():
    data = servListCorreo()
    return jsonify(data), 200


def cntCreateCorreo():
    body = request.get_json()

    user_id = body.get("user_id")
    correo  = body.get("correo")

    if not user_id or not correo:
        return jsonify({"error": "user_id y correo son obligatorios"}), 400

    if searchByCorreo(correo) is not None:
        return jsonify({"error": "El correo ya está registrado"}), 409

    nuevo_correo = addCorreo(user_id, correo)
    return jsonify(nuevo_correo), 201


def cntUpdateCorreo():
    body = request.get_json()

    id      = body.get("id")
    correo  = body.get("correo")

    if not id or not correo:
        return jsonify({"error": "id y correo son obligatorios"}), 400

    filas_afectadas = upCorreo(id, correo)

    if filas_afectadas == 0:
        return jsonify({"error": "Correo no encontrado"}), 404

    return jsonify({"mensaje": "Correo actualizado correctamente"}), 200


def cntDeleteCorreo():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delCorreo(id)

    if filas_afectadas == 0:
        return jsonify({"error": "Correo no encontrado"}), 404

    return jsonify({"mensaje": "Correo eliminado correctamente"}), 200


def cntListCorreosByUser(user_id):
    data = servListCorreoByUser(user_id)
    return jsonify(data), 200