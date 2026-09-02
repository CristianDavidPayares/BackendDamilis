from flask import jsonify, request
from Services.ProductoService import ProductoService


class ProductoController:

    def listar():
        data = ProductoService.listar()
        return jsonify(data), 200


    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        codigo = body.get("codigo")
        talla = body.get("talla")
        color = body.get("color")
        resena = body.get("resena")
        descripcion = body.get("descripcion")
        precio = body.get("precio")
        calificacion = body.get("calificacion")
        imagen = body.get("imagen")
        cantidad = body.get("cantidad")

        # Validar obligatorios
        if codigo is None or precio is None or cantidad is None:
            return jsonify({
                "error": "codigo, precio y cantidad son obligatorios"
            }), 400

        # Validar código (string no vacío)
        if not isinstance(codigo, str) or not codigo.strip():
            return jsonify({
                "error": "codigo debe ser una cadena de texto válida"
            }), 400
        codigo = codigo.strip()

        # Validar precio (número >= 0)
        try:
            precio = float(precio)
            if precio < 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "precio debe ser un número mayor o igual a 0"
            }), 400

        # Validar cantidad (entero >= 0)
        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad debe ser un entero mayor o igual a 0"
            }), 400

        # Validar calificación (opcional, si viene debe ser número entre 0 y 5)
        if calificacion is not None:
            try:
                calificacion = float(calificacion)
                if calificacion < 0 or calificacion > 5:
                    raise ValueError
            except (ValueError, TypeError):
                return jsonify({
                    "error": "calificacion debe ser un número entre 0 y 5"
                }), 400

        # Validar talla, color, reseña, descripción e imagen (si existen, deben ser strings)
        for campo, nombre in [(talla, "talla"), (color, "color"), (resena, "resena"),
                              (descripcion, "descripcion"), (imagen, "imagen")]:
            if campo is not None and (not isinstance(campo, str) or not campo.strip()):
                return jsonify({
                    "error": f"{nombre} debe ser una cadena de texto válida"
                }), 400

        # Verificar duplicado de código
        if ProductoService.buscarPorCodigo(codigo) is not None:
            return jsonify({
                "error": "Ya existe un producto con ese código"
            }), 409

        nuevo_producto = ProductoService.crear(
            codigo, talla, color, resena, descripcion,
            precio, calificacion, imagen, cantidad
        )
        return jsonify(nuevo_producto), 201


    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        codigo = body.get("codigo")
        talla = body.get("talla")
        color = body.get("color")
        resena = body.get("resena")
        descripcion = body.get("descripcion")
        precio = body.get("precio")
        calificacion = body.get("calificacion")
        imagen = body.get("imagen")
        cantidad = body.get("cantidad")

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

        # Validar código (si viene)
        if codigo is not None:
            if not isinstance(codigo, str) or not codigo.strip():
                return jsonify({
                    "error": "codigo debe ser una cadena de texto válida"
                }), 400
            codigo = codigo.strip()
            # Verificar duplicado solo si se cambia el código
            existente = ProductoService.buscarPorCodigo(codigo)
            if existente is not None and existente["pro_id"] != id:
                return jsonify({
                    "error": "Ya existe un producto con ese código"
                }), 409

        # Validar precio (si viene)
        if precio is not None:
            try:
                precio = float(precio)
                if precio < 0:
                    raise ValueError
            except (ValueError, TypeError):
                return jsonify({
                    "error": "precio debe ser un número mayor o igual a 0"
                }), 400

        # Validar cantidad (si viene)
        if cantidad is not None:
            try:
                cantidad = int(cantidad)
                if cantidad < 0:
                    raise ValueError
            except (ValueError, TypeError):
                return jsonify({
                    "error": "cantidad debe ser un entero mayor o igual a 0"
                }), 400

        # Validar calificación (si viene)
        if calificacion is not None:
            try:
                calificacion = float(calificacion)
                if calificacion < 0 or calificacion > 5:
                    raise ValueError
            except (ValueError, TypeError):
                return jsonify({
                    "error": "calificacion debe ser un número entre 0 y 5"
                }), 400

        # Validar campos de texto (si vienen)
        for campo, nombre in [(talla, "talla"), (color, "color"), (resena, "resena"),
                              (descripcion, "descripcion"), (imagen, "imagen")]:
            if campo is not None and (not isinstance(campo, str) or not campo.strip()):
                return jsonify({
                    "error": f"{nombre} debe ser una cadena de texto válida"
                }), 400

        filas_afectadas = ProductoService.actualizar(
            id, codigo, talla, color, resena, descripcion,
            precio, calificacion, imagen, cantidad
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Producto actualizado correctamente"
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

        filas_afectadas = ProductoService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Producto eliminado correctamente"
        }), 200


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
        producto = ProductoService.buscarPorCodigo(codigo)

        if producto is None:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify(producto), 200


    def actualizarCantidad():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        cantidad = body.get("cantidad")

        if id is None or cantidad is None:
            return jsonify({
                "error": "id y cantidad son obligatorios"
            }), 400

        try:
            id = int(id)
            if id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "id debe ser un entero positivo"
            }), 400

        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({
                "error": "cantidad debe ser un entero mayor o igual a 0"
            }), 400

        filas_afectadas = ProductoService.actualizarCantidad(id, cantidad)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Producto no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Cantidad actualizada correctamente"
        }), 200