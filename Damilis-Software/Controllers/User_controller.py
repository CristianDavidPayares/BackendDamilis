from flask import jsonify, request
from Services.User_services import servListUser, addUser, upUser, delUser, searchByDoc


class UserController:

   
    def Listar():
        data = servListUser()
        return jsonify(data), 200

    
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        campos_requeridos = [
            "cedula",
            "primer_nombre",
            "primer_apellido",
            "segundo_apellido"
        ]

        campos_faltantes = [
            campo for campo in campos_requeridos
            if campo not in body
        ]

        if campos_faltantes:
            return jsonify({
                "error": "Campos faltantes",
                "campos": campos_faltantes
            }), 400

        cedula = body.get("cedula")
        primer_nombre = body.get("primer_nombre")
        segundo_nombre = body.get("segundo_nombre")
        primer_apellido = body.get("primer_apellido")
        segundo_apellido = body.get("segundo_apellido")

        if not cedula or not primer_nombre or not primer_apellido:
            return jsonify({
                "error": "cedula, primer_nombre y primer_apellido son obligatorios"
            }), 400

        nuevo_usuario = addUser(
            cedula,
            primer_nombre,
            segundo_nombre,
            primer_apellido,
            segundo_apellido
        )

        return jsonify(nuevo_usuario), 201

    
    def update():
        body = request.get_json()

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        campos_requeridos = [
            "id",
            "cedula",
            "primer_nombre",
            "primer_apellido"
        ]

        campos_faltantes = [
            campo for campo in campos_requeridos
            if campo not in body
        ]

        if campos_faltantes:
            return jsonify({
                "error": "Campos faltantes",
                "campos": campos_faltantes
            }), 400

        id = body.get("id")
        cedula = body.get("cedula")
        primer_nombre = body.get("primer_nombre")
        segundo_nombre = body.get("segundo_nombre")
        primer_apellido = body.get("primer_apellido")
        segundo_apellido = body.get("segundo_apellido")

        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = upUser(
            id,
            cedula,
            primer_nombre,
            segundo_nombre,
            primer_apellido,
            segundo_apellido
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Usuario actualizado correctamente"
        }), 200

    
    def delete(id):
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

    
    def SearchByDoc(cedula):
        usuario = searchByDoc(cedula)

        if usuario is None:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404

        return jsonify(usuario), 200
