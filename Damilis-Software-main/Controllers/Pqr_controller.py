from flask import jsonify, request
from Services.Pqr_services import (
    servListPqr,
    addPqr,
    upPqr,
    delPqr,
    servListPqrByCliente,
    responderPqr
)


class PqrController:

    # Listar todas las PQR
    def ListPqrs():
        data = servListPqr()
        return jsonify(data), 200

    # Crear una PQR
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        descripcion = body.get("descripcion")
        cli_id = body.get("cli_id")

        if not descripcion or not cli_id:
            return jsonify({
                "error": "descripcion y cli_id son obligatorios"
            }), 400

        nueva_pqr = addPqr(
            descripcion,
            cli_id
        )

        return jsonify(nueva_pqr), 201

    # Actualizar una PQR
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        descripcion = body.get("descripcion")

        if not id or not descripcion:
            return jsonify({
                "error": "id y descripcion son obligatorios"
            }), 400

        filas_afectadas = upPqr(
            id,
            descripcion
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "PQR no encontrada"
            }), 404

        return jsonify({
            "mensaje": "PQR actualizada correctamente"
        }), 200

    # Eliminar una PQR
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delPqr(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "PQR no encontrada"
            }), 404

        return jsonify({
            "mensaje": "PQR eliminada correctamente"
        }), 200

    # Listar PQR por cliente
    def ListPqrsByCliente(cli_id):
        data = servListPqrByCliente(cli_id)
        return jsonify(data), 200

    # Responder una PQR
    def ResponderPqr():
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

        filas_afectadas = responderPqr(
            id,
            estado
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "PQR no encontrada"
            }), 404

        return jsonify({
            "mensaje": "PQR respondida correctamente"
        }), 200