from flask import jsonify, request
from Services.Telefono_services import (
    servListTelefono,
    addTelefono,
    upTelefono,
    delTelefono,
    servListTelefonoByUser
)


def cntListTelefonos():
    data = servListTelefono()
    return jsonify(data), 200


def cntCreateTelefono():
    body = request.get_json()

    user_id     = body.get("user_id")
    telefono    = body.get("telefono")

    if not user_id or not telefono:
        return jsonify({"error": "user_id y telefono son obligatorios"}), 400

    nuevo_telefono = addTelefono(user_id, telefono)
    return jsonify(nuevo_telefono), 201


def cntUpdateTelefono():
    body = request.get_json()

    id          = body.get("id")
    telefono    = body.get("telefono")

    if not id or not telefono:
        return jsonify({"error": "id y telefono son obligatorios"}), 400

    filas_afectadas = upTelefono(id, telefono)

    if filas_afectadas == 0:
        return jsonify({"error": "Teléfono no encontrado"}), 404

    return jsonify({"mensaje": "Teléfono actualizado correctamente"}), 200


def cntDeleteTelefono():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delTelefono(id)

    if filas_afectadas == 0:
        return jsonify({"error": "Teléfono no encontrado"}), 404

    return jsonify({"mensaje": "Teléfono eliminado correctamente"}), 200


def cntListTelefonosByUser(user_id):
    data = servListTelefonoByUser(user_id)
    return jsonify(data), 200