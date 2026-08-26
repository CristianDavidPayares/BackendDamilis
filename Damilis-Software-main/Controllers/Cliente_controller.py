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


def cntListClientes():
    data = servListCliente()
    return jsonify(data), 200


def cntCreateCliente():
    body = request.get_json()

    preferencias    = body.get("preferencias")
    per_cedula      = body.get("per_cedula")
    user_id         = body.get("user_id")

    if not per_cedula or not user_id:
        return jsonify({"error": "per_cedula y user_id son obligatorios"}), 400

    if searchByCedula(per_cedula) is not None:
        return jsonify({"error": "Ya existe un cliente con esa cédula"}), 409

    nuevo_cliente = addCliente(preferencias, per_cedula, user_id)
    return jsonify(nuevo_cliente), 201


def cntUpdateCliente():
    body = request.get_json()

    id              = body.get("id")
    preferencias    = body.get("preferencias")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = upCliente(id, preferencias)

    if filas_afectadas == 0:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify({"mensaje": "Cliente actualizado correctamente"}), 200


def cntDeleteCliente():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delCliente(id)

    if filas_afectadas == 0:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify({"mensaje": "Cliente eliminado correctamente"}), 200


def cntCambiarEstado():
    body = request.get_json()

    id      = body.get("id")
    estado  = body.get("estado")

    if not id or not estado:
        return jsonify({"error": "id y estado son obligatorios"}), 400

    filas_afectadas = cambiarEstado(id, estado)

    if filas_afectadas == 0:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify({"mensaje": "Estado actualizado correctamente"}), 200


def cntSearchByCedula(per_cedula):
    cliente = searchByCedula(per_cedula)

    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(cliente), 200


def cntSearchByUserId(user_id):
    cliente = searchByUserId(user_id)

    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(cliente), 200