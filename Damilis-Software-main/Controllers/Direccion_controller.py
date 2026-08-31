from flask import jsonify, request
from Services.Direccion_services import (
    servListDireccion,
    addDireccion,
    upDireccion,
    delDireccion,
    servListDireccionByUser
)

DIRECCION_MIN_LEN = 5


def cntListDirecciones():
    data = servListDireccion()
    return jsonify(data), 200


def cntCreateDireccion():
    body = request.get_json()

    user_id     = body.get("user_id")
    direccion   = body.get("direccion")

    if not user_id or not direccion:
        return jsonify({"error": "user_id y direccion son obligatorios"}), 400

<<<<<<< Updated upstream
    nueva_direccion = addDireccion(user_id, direccion)
    return jsonify(nueva_direccion), 201


def cntUpdateDireccion():
    body = request.get_json()
=======
        if user_id is None or not direccion:
            return jsonify({
                "error": "user_id y direccion son obligatorios"
            }), 400

        try:
            user_id = int(user_id)
            if user_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "user_id debe ser un entero positivo"
            }), 400

        if not isinstance(direccion, str) or not direccion.strip():
            return jsonify({
                "error": "direccion debe ser una cadena de texto válida"
            }), 400
        direccion = direccion.strip()

        if len(direccion) < DIRECCION_MIN_LEN:
            return jsonify({
                "error": f"direccion debe tener al menos {DIRECCION_MIN_LEN} caracteres"
            }), 400

        nueva_direccion = addDireccion(user_id, direccion)
        return jsonify(nueva_direccion), 201
>>>>>>> Stashed changes

    id          = body.get("id")
    direccion   = body.get("direccion")

    if not id or not direccion:
        return jsonify({"error": "id y direccion son obligatorios"}), 400

    filas_afectadas = upDireccion(id, direccion)

<<<<<<< Updated upstream
    if filas_afectadas == 0:
        return jsonify({"error": "Dirección no encontrada"}), 404

    return jsonify({"mensaje": "Dirección actualizada correctamente"}), 200
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

        if not direccion:
            return jsonify({
                "error": "direccion es obligatoria para actualizar"
            }), 400

        if not isinstance(direccion, str) or not direccion.strip():
            return jsonify({
                "error": "direccion debe ser una cadena de texto válida"
            }), 400
        direccion = direccion.strip()

        if len(direccion) < DIRECCION_MIN_LEN:
            return jsonify({
                "error": f"direccion debe tener al menos {DIRECCION_MIN_LEN} caracteres"
            }), 400

        filas_afectadas = upDireccion(id, direccion)
>>>>>>> Stashed changes


def cntDeleteDireccion():
    body = request.get_json()
    id = body.get("id")

<<<<<<< Updated upstream
    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delDireccion(id)
=======
    # Eliminar una dirección
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

        filas_afectadas = delDireccion(id)
>>>>>>> Stashed changes

    if filas_afectadas == 0:
        return jsonify({"error": "Dirección no encontrada"}), 404

    return jsonify({"mensaje": "Dirección eliminada correctamente"}), 200

<<<<<<< Updated upstream

def cntListDireccionesByUser(user_id):
    data = servListDireccionByUser(user_id)
    return jsonify(data), 200
=======
    # Listar direcciones de un usuario
    def ListDireccionesByUser(user_id):
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

        data = servListDireccionByUser(user_id)
        return jsonify(data), 200
>>>>>>> Stashed changes
