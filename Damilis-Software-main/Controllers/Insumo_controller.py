from flask import jsonify, request
from Services.Insumo_services import (
    servListInsumo,
    addInsumo,
    upInsumo,
    delInsumo,
    searchByCodigo,
    servListInsumoByTipo
)


def cntListInsumos():
    data = servListInsumo()
    return jsonify(data), 200


def cntCreateInsumo():
    body = request.get_json()

    codigo          = body.get("codigo")
    tipo_insumo     = body.get("tipo_insumo")
    unidad_medida   = body.get("unidad_medida")
    color           = body.get("color")

    if not codigo or not tipo_insumo:
        return jsonify({"error": "codigo y tipo_insumo son obligatorios"}), 400

    nuevo_insumo = addInsumo(codigo, tipo_insumo, unidad_medida, color)
    return jsonify(nuevo_insumo), 201


def cntUpdateInsumo():
    body = request.get_json()

    id              = body.get("id")
    codigo          = body.get("codigo")
    tipo_insumo     = body.get("tipo_insumo")
    unidad_medida   = body.get("unidad_medida")
    color           = body.get("color")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = upInsumo(id, codigo, tipo_insumo, unidad_medida, color)

    if filas_afectadas == 0:
        return jsonify({"error": "Insumo no encontrado"}), 404

    return jsonify({"mensaje": "Insumo actualizado correctamente"}), 200


def cntDeleteInsumo():
    body = request.get_json()
    id = body.get("id")

    if not id:
        return jsonify({"error": "id es obligatorio"}), 400

    filas_afectadas = delInsumo(id)

    if filas_afectadas == 0:
        return jsonify({"error": "Insumo no encontrado"}), 404

    return jsonify({"mensaje": "Insumo eliminado correctamente"}), 200


def cntSearchByCodigo(codigo):
    insumo = searchByCodigo(codigo)

    if insumo is None:
        return jsonify({"error": "Insumo no encontrado"}), 404

    return jsonify(insumo), 200


def cntListInsumosByTipo(tipo_insumo):
    data = servListInsumoByTipo(tipo_insumo)
    return jsonify(data), 200