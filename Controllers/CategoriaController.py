from flask import jsonify, request
from Services.CategoriaService import CategoriaService


class CategoriaController:

    # Listar todas las categorías
    def listar():
        data = CategoriaService.listar()
        return jsonify(data), 200

    # Buscar categoría por tipo
    def buscarPorTipo(tipo_categoria):
        categoria = CategoriaService.buscarPorTipo(tipo_categoria)

        if categoria is None:
            return jsonify({
                "error": "Categoría no encontrada"
            }), 404

        return jsonify(categoria), 200

    # Crear una categoría
    def crear():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        tipo_categoria = body.get("tipo_categoria")

        # Validar que no esté vacío
        if not tipo_categoria or not str(tipo_categoria).strip():
            return jsonify({
                "error": "tipo_categoria es obligatorio y no puede estar vacío"
            }), 400

        # Eliminar espacios al inicio y al final
        tipo_categoria = str(tipo_categoria).strip()

        # Verificar que no exista otra categoría igual
        if CategoriaService.buscarPorTipo(tipo_categoria) is not None:
            return jsonify({
                "error": "Ya existe una categoría con ese tipo"
            }), 409

        nueva_categoria = CategoriaService.crear(tipo_categoria)

        return jsonify(nueva_categoria), 201

    # Actualizar una categoría
    def actualizar():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        tipo_categoria = body.get("tipo_categoria")

        # Validar ID
        if id is None:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        # Validar tipo de categoría
        if not tipo_categoria or not str(tipo_categoria).strip():
            return jsonify({
                "error": "tipo_categoria es obligatorio y no puede estar vacío"
            }), 400

        # Eliminar espacios al inicio y al final
        tipo_categoria = str(tipo_categoria).strip()

        # Verificar que no exista otra categoría con el mismo tipo
        categoria_existente = CategoriaService.buscarPorTipo(tipo_categoria)

        if categoria_existente is not None and categoria_existente["id"] != id:
            return jsonify({
                "error": "Ya existe una categoría con ese tipo"
            }), 409

        filas_afectadas = CategoriaService.actualizar(
            id,
            tipo_categoria
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Categoría no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Categoría actualizada correctamente"
        }), 200

    # Eliminar una categoría
    def eliminar(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = CategoriaService.eliminar(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Categoría no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Categoría eliminada correctamente"
        }), 200