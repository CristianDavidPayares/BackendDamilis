from flask import jsonify, request
from Services.InsumoService import InsumoService


class InsumoController:

    # Listar todos los insumos
    def listar():
        data = InsumoService.listar()
        return jsonify(data), 200


    # Crear un insumo
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        codigo = body.get("codigo")
        tipo_insumo = body.get("tipo_insumo")
        unidad_medida = body.get("unidad_medida")
        color = body.get("color")

        # Validar campos obligatorios
        if codigo is None or tipo_insumo is None:
            return jsonify({
                "error": "codigo y tipo_insumo son obligatorios"
            }), 400

        # Validar codigo (string no vacío)
        if not isinstance(codigo, str) or not codigo.strip():
            return jsonify({
                "error": "codigo debe ser una cadena de texto válida"
            }), 400

        codigo = codigo.strip()

        # Validar tipo_insumo (string no vacío)
        if not isinstance(tipo_insumo, str) or not tipo_insumo.strip():
            return jsonify({
                "error": "tipo_insumo debe ser una cadena de texto válida"
            }), 400

        tipo_insumo = tipo_insumo.strip()

        # Validar unidad_medida (opcional, si viene se valida)
        if unidad_medida is not None:
            if not isinstance(unidad_medida, str) or not unidad_medida.strip():
                return jsonify({
                    "error": "unidad_medida debe ser una cadena de texto válida"
                }), 400
            unidad_medida = unidad_medida.strip()

        # Validar color (opcional, si viene se valida)
        if color is not None:
            if not isinstance(color, str) or not color.strip():
                return jsonify({
                    "error": "color debe ser una cadena de texto válida"
                }), 400
            color = color.strip()

        # Verificar si ya existe un insumo con ese código
        if InsumoService.buscarPorCodigo(codigo) is not None:
            return jsonify({
                "error": "Ya existe un insumo con ese código"
            }), 409

        nuevo_insumo = InsumoService.crear(codigo, tipo_insumo, unidad_medida, color)
        return jsonify(nuevo_insumo), 201


    # Actualizar un insumo
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        codigo = body.get("codigo")
        tipo_insumo = body.get("tipo_insumo")
        unidad_medida = body.get("unidad_medida")
        color = body.get("color")

        # Validar id
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

        # Validar campos obligatorios
        if codigo is None or tipo_insumo is None:
            return jsonify({
                "error": "codigo y tipo_insumo son obligatorios"
            }), 400

        # Validar codigo (string no vacío)
        if not isinstance(codigo, str) or not codigo.strip():
            return jsonify({
                "error": "codigo debe ser una cadena de texto válida"
            }), 400

        codigo = codigo.strip()

        # Validar tipo_insumo (string no vacío)
        if not isinstance(tipo_insumo, str) or not tipo_insumo.strip():
            return jsonify({
                "error": "tipo_insumo debe ser una cadena de texto válida"
            }), 400

        tipo_insumo = tipo_insumo.strip()

        # Validar unidad_medida (opcional, si viene se valida)
        if unidad_medida is not None:
            if not isinstance(unidad_medida, str) or not unidad_medida.strip():
                return jsonify({
                    "error": "unidad_medida debe ser una cadena de texto válida"
                }), 400
            unidad_medida = unidad_medida.strip()

        # Validar color (opcional, si viene se valida)
        if color is not None:
            if not isinstance(color, str) or not color.strip():
                return jsonify({
                    "error": "color debe ser una cadena de texto válida"
                }), 400
            color = color.strip()

        filas_afectadas = InsumoService.actualizar(id, codigo, tipo_insumo, unidad_medida, color)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Insumo actualizado correctamente"
        }), 200


    # Eliminar un insumo
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

        filas_afectadas = InsumoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Insumo eliminado correctamente"
        }), 200


    # Buscar insumo por código
    def buscarPorCodigo(codigo):
        if codigo is None:
            return jsonify({
                "error": "codigo es obligatorio"
            }), 400

        if not isinstance(codigo, str) or not codigo.strip():
            return jsonify({
                "error": "codigo debe ser una cadena de texto válida"
            }), 400

        codigo = codigo.strip()
        insumo = InsumoService.buscarPorCodigo(codigo)

        if insumo is None:
            return jsonify({
                "error": "Insumo no encontrado"
            }), 404

        return jsonify(insumo), 200


    # Listar insumos por tipo
    def listarPorTipo(tipo_insumo):
        if tipo_insumo is None:
            return jsonify({
                "error": "tipo_insumo es obligatorio"
            }), 400

        if not isinstance(tipo_insumo, str) or not tipo_insumo.strip():
            return jsonify({
                "error": "tipo_insumo debe ser una cadena de texto válida"
            }), 400

        tipo_insumo = tipo_insumo.strip()
        data = InsumoService.listarPorTipo(tipo_insumo)
        return jsonify(data), 200