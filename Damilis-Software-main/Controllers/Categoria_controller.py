from flask import jsonify, request
from Services.Categoria_services import (
    servListCategoria,
    addCategoria,
    upCategoria,
    delCategoria,
    searchByTipo
)


class CategoriaController:

    # Listar todas las categorías
    def ListCategorias():
        data = servListCategoria()
        return jsonify(data), 200

    # Crear una categoría
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        tipo_categoria = body.get("tipo_categoria")

        if not tipo_categoria:
            return jsonify({
                "error": "tipo_categoria es obligatorio"
            }), 400

        if searchByTipo(tipo_categoria) is not None:
            return jsonify({
                "error": "Ya existe una categoría con ese tipo"
            }), 409

        nueva_categoria = addCategoria(tipo_categoria)

        return jsonify(nueva_categoria), 201

    # Actualizar una categoría
    def update():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        tipo_categoria = body.get("tipo_categoria")

        if not id or not tipo_categoria:
            return jsonify({
                "error": "id y tipo_categoria son obligatorios"
            }), 400

        filas_afectadas = upCategoria(
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
    
    # Buscar una categoría por tipo
    def SearchByTipo(tipo_categoria):
        categoria = searchByTipo(tipo_categoria)

        if categoria is None:
            return jsonify({
                "error": "Categoría no encontrada"
            }), 404

        return jsonify(categoria), 200

    # Eliminar una categoría
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delCategoria(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Categoría no encontrada"
            }), 404

        return jsonify({
            "mensaje": "Categoría eliminada correctamente"
        }), 200
