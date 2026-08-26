from flask import jsonify, request
from Services.Direccion_services import (
    servListDireccion,
    addDireccion,
    upDireccion,
    delDireccion,
    servListDireccionByUser
)


def cntListDirecciones():
    data = servListDireccion()
    return jsonify(data), 200


def cntCreateDireccion():
    body = request.get_json()

    user_id     = body.get("user_id")
    direccion   = body.get("direccion")

    if not user_id or not direccion:
        return jsonify({"error": "user_id y direccion son obligatorios"}), 400

    nueva_direccion = addDireccion(user_id, direccion)
    return jsonify(nueva_direccion), 201


def cntUpdateDireccion():
    body = request.get_json()

    id          = body.get("id")
    direccion   = body.get("direccion")

    if not id or not direccion:
        return jsonify({"error": "id y direccion son obligatorios"}), 400

    filas_afectadas = upDireccion(id, direccion)

    if filas_afectadas == 0:
        return jsonify({"error": "Dirección no encontrada"}), 404

    return jsonify({"mensaje": "Dirección actualizada correctamente"}), 200


def cntDeleteDireccion():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delDireccion(id)

    if filas_afectadas == 0:
        return jsonify({"error": "Dirección no encontrada"}), 404

    return jsonify({"mensaje": "Dirección eliminada correctamente"}), 200


def cntListDireccionesByUser(user_id):
    data = servListDireccionByUser(user_id)
    return jsonify(data), 200