from flask import jsonify, request
from Services.User_services import servListUser, addUser, upUser, delUser, searchByDoc


def cntListUsers():
    data = servListUser()
    return jsonify(data), 200


def cntCreateUser():
    body = request.get_json()

    cedula              = body.get("cedula")
    primer_nombre       = body.get("primer_nombre")
    segundo_nombre      = body.get("segundo_nombre")
    primer_apellido     = body.get("primer_apellido")
    segundo_apellido    = body.get("segundo_apellido")

    if not cedula or not primer_nombre or not primer_apellido:
        return jsonify({"error": "cedula, primer_nombre y primer_apellido son obligatorios"}), 400

    nuevo_usuario = addUser(cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)
    return jsonify(nuevo_usuario), 201


def cntUpdateUser():
    body = request.get_json()

    id                  = body.get("id")
    cedula              = body.get("cedula")
    primer_nombre       = body.get("primer_nombre")
    segundo_nombre      = body.get("segundo_nombre")
    primer_apellido     = body.get("primer_apellido")
    segundo_apellido    = body.get("segundo_apellido")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = upUser(id, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)

    if filas_afectadas == 0:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200


# def cntDeleteUser():
#     body = request.get_json()
#     id = body.get("id")

#     if not id:
#         return jsonify({"error": "id es obligatorio"}), 400

#     filas_afectadas = delUser(id)

#     if filas_afectadas == 0:
#         return jsonify({"error": "Usuario no encontrado"}), 404

#     return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200

def cntDeleteUser(id):

    if not id:
        return jsonify({
            "error": "id es obligatorio"
        }), 400

    filas_afectadas = delUser(id)

    if filas_afectadas == 0:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Usuario eliminado correctamente"
    }), 200


def cntSearchByDoc(cedula):

    usuario = searchByDoc(cedula)

    if usuario is None:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify(usuario), 200