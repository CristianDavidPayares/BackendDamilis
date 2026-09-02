from flask import jsonify, request
from Services.UserService import UsuarioService


class UsuarioController:

    def listar():
        data = UsuarioService.listar()
        return jsonify(data), 200


    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        cedula = body.get("cedula")
        primer_nombre = body.get("primer_nombre")
        segundo_nombre = body.get("segundo_nombre")
        primer_apellido = body.get("primer_apellido")
        segundo_apellido = body.get("segundo_apellido")

        # Validar campos obligatorios
        if cedula is None or primer_nombre is None or primer_apellido is None:
            return jsonify({
                "error": "cedula, primer_nombre y primer_apellido son obligatorios"
            }), 400

        # Validar cédula (entero positivo)
        try:
            cedula = int(cedula)
            if cedula <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "cedula debe ser un entero positivo"
            }), 400

        # Validar nombres y apellidos (strings no vacíos)
        for campo, nombre in [(primer_nombre, "primer_nombre"),
                              (primer_apellido, "primer_apellido")]:
            if not isinstance(campo, str) or not campo.strip():
                return jsonify({
                    "error": f"{nombre} debe ser una cadena de texto válida"
                }), 400

        # Campos opcionales
        if segundo_nombre is not None:
            if not isinstance(segundo_nombre, str) or not segundo_nombre.strip():
                return jsonify({
                    "error": "segundo_nombre debe ser una cadena de texto válida"
                }), 400
        if segundo_apellido is not None:
            if not isinstance(segundo_apellido, str) or not segundo_apellido.strip():
                return jsonify({
                    "error": "segundo_apellido debe ser una cadena de texto válida"
                }), 400

        # Verificar duplicado de cédula
        if UsuarioService.buscarPorCedula(cedula) is not None:
            return jsonify({
                "error": "Ya existe un usuario con esa cédula"
            }), 409

        nuevo_usuario = UsuarioService.crear(
            cedula,
            primer_nombre.strip(),
            segundo_nombre.strip() if segundo_nombre else None,
            primer_apellido.strip(),
            segundo_apellido.strip() if segundo_apellido else None
        )
        return jsonify(nuevo_usuario), 201


    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        cedula = body.get("cedula")
        primer_nombre = body.get("primer_nombre")
        segundo_nombre = body.get("segundo_nombre")
        primer_apellido = body.get("primer_apellido")
        segundo_apellido = body.get("segundo_apellido")

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

        # Validar cédula (si viene)
        if cedula is not None:
            try:
                cedula = int(cedula)
                if cedula <= 0:
                    raise ValueError
            except (ValueError, TypeError):
                return jsonify({
                    "error": "cedula debe ser un entero positivo"
                }), 400
            # Verificar duplicado solo si se cambia la cédula
            existente = UsuarioService.buscarPorCedula(cedula)
            if existente is not None and existente["user_id"] != id:
                return jsonify({
                    "error": "Ya existe un usuario con esa cédula"
                }), 409

        # Validar campos de texto (si vienen)
        for campo, nombre in [(primer_nombre, "primer_nombre"),
                              (primer_apellido, "primer_apellido")]:
            if campo is not None and (not isinstance(campo, str) or not campo.strip()):
                return jsonify({
                    "error": f"{nombre} debe ser una cadena de texto válida"
                }), 400

        if segundo_nombre is not None and (not isinstance(segundo_nombre, str) or not segundo_nombre.strip()):
            return jsonify({
                "error": "segundo_nombre debe ser una cadena de texto válida"
            }), 400

        if segundo_apellido is not None and (not isinstance(segundo_apellido, str) or not segundo_apellido.strip()):
            return jsonify({
                "error": "segundo_apellido debe ser una cadena de texto válida"
            }), 400

        # Si no se envían campos para actualizar, devolver error
        if (cedula is None and primer_nombre is None and segundo_nombre is None and
            primer_apellido is None and segundo_apellido is None):
            return jsonify({
                "error": "No se enviaron campos para actualizar"
            }), 400

        filas_afectadas = UsuarioService.actualizar(
            id,
            cedula,
            primer_nombre.strip() if primer_nombre else None,
            segundo_nombre.strip() if segundo_nombre else None,
            primer_apellido.strip() if primer_apellido else None,
            segundo_apellido.strip() if segundo_apellido else None
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Usuario actualizado correctamente"
        }), 200


    def eliminar(id):
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

        filas_afectadas = UsuarioService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Usuario eliminado correctamente"
        }), 200


    def buscarPorCedula(cedula):
        if cedula is None:
            return jsonify({
                "error": "cedula es obligatoria"
            }), 400

        try:
            cedula = int(cedula)
            if cedula <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "cedula debe ser un entero positivo"
            }), 400

        usuario = UsuarioService.buscarPorCedula(cedula)

        if usuario is None:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404

        return jsonify(usuario), 200