from flask import jsonify, request
from Services.Pqr_services import (
    servListPqr,
    addPqr,
    upPqr,
    delPqr,
    servListPqrByCliente,
    responderPqr
)


def cntListPqrs():
    data = servListPqr()
    return jsonify(data), 200


def cntCreatePqr():
    body = request.get_json()

    descripcion = body.get("descripcion")
    cli_id      = body.get("cli_id")

    if not descripcion or not cli_id:
        return jsonify({"error": "descripcion y cli_id son obligatorios"}), 400

    nueva_pqr = addPqr(descripcion, cli_id)
    return jsonify(nueva_pqr), 201


def cntUpdatePqr():
    body = request.get_json()

    id          = body.get("id")
    descripcion = body.get("descripcion")

    if not id or not descripcion:
        return jsonify({"error": "id y descripcion son obligatorios"}), 400

    filas_afectadas = upPqr(id, descripcion)

    if filas_afectadas == 0:
        return jsonify({"error": "PQR no encontrada"}), 404

    return jsonify({"mensaje": "PQR actualizada correctamente"}), 200


def cntDeletePqr():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delPqr(id)

    if filas_afectadas == 0:
        return jsonify({"error": "PQR no encontrada"}), 404

    return jsonify({"mensaje": "PQR eliminada correctamente"}), 200


def cntListPqrsByCliente(cli_id):
    data = servListPqrByCliente(cli_id)
    return jsonify(data), 200


def cntResponderPqr():
    body = request.get_json()

    id      = body.get("id")
    estado  = body.get("estado")

    if not id or not estado:
        return jsonify({"error": "id y estado son obligatorios"}), 400

    filas_afectadas = responderPqr(id, estado)

    if filas_afectadas == 0:
        return jsonify({"error": "PQR no encontrada"}), 404

    return jsonify({"mensaje": "PQR respondida correctamente"}), 200