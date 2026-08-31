
from flask import jsonify, request
from Services.Insumo_services import (
    servListInsumo,
    addInsumo,
    upInsumo,
    delInsumo,
    searchByCodigo,
    servListInsumoByTipo
)


class InsumoController:

    # Listar todos los insumos
    def ListInsumos():
        data = servListInsumo()
        return jsonify(data), 200

    # Crear un insumo
    def create():
        body = request.get_json(silent=True)

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        codigo = body.get("codigo")
        tipo_insumo = body.get("tipo_insumo")
        unidad_medida = body.get("unidad_medida")
        color = body.get("color")

        nuevo_insumo = addInsumo(
            codigo,
            tipo_insumo,
            unidad_medida,
            color
        )

        return jsonify(nuevo_insumo), 201

    # Actualizar un insumo
    def cntUpdateInsumo():
        body = request.get_json()

        if not body:
            return jsonify({
                "error": "El cuerpo de la petición es obligatorio"
            }), 400

        id = body.get("id")
        codigo = body.get("codigo")
        tipo_insumo = body.get("tipo_insumo")
        unidad_medida = body.get("unidad_medida")
        color = body.get("color")

        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        if not codigo or not tipo_insumo:
            return jsonify({
                "error": "id, codigo y tipo_insumo son obligatorios"
            }), 400

        filas_afectadas = upInsumo(
            id,
            codigo,
            tipo_insumo,
            unidad_medida,
            color
        )

        if filas_afectadas == 0:
            return jsonify({
                "error": "Insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Insumo actualizado correctamente"
        }), 200

    # Eliminar un insumo
    def delete(id):
        if not id:
            return jsonify({
                "error": "id es obligatorio"
            }), 400

        filas_afectadas = delInsumo(id)

        if filas_afectadas == 0:
            return jsonify({
                "error": "Insumo no encontrado"
            }), 404

        return jsonify({
            "mensaje": "Insumo eliminado correctamente"
        }), 200

    # Buscar insumo por código
    def SearchByCodigo(codigo):
        insumo = searchByCodigo(codigo)

        if insumo is None:
            return jsonify({
                "error": "Insumo no encontrado"
            }), 404

        return jsonify(insumo), 200

    # Listar insumos por tipo
    def ListInsumosByTipo(tipo_insumo):
        data = servListInsumoByTipo(tipo_insumo)
        return jsonify(data), 200

