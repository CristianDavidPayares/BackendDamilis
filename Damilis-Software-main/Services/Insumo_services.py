from flask import current_app
from Models.Insumo import Insumo
import uuid


def servListInsumo():
    sql = "SELECT * FROM T_INSUMO"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()

    insumos_l = []
    for i in data:
        insumos_l.append(Insumo(i[0], i[1], i[2], i[3], i[4], i[5]).to_dic())

    c.close()
    return insumos_l


def addInsumo(codigo, tipo_insumo, unidad_medida, color):
    ins_uuid = str(uuid.uuid4())
    sql = """
        INSERT INTO T_INSUMO
        (INS_UUID, INS_CODIGO, INS_TIPO_INSUMO, INS_UNIDAD_MEDIDA, INS_COLOR)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (ins_uuid, codigo, tipo_insumo, unidad_medida, color)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    new_id = c.lastrowid
    c.close()

    return Insumo(new_id, ins_uuid, codigo, tipo_insumo, unidad_medida, color).to_dic()


def upInsumo(id, codigo, tipo_insumo, unidad_medida, color):
    sql = """
        UPDATE T_INSUMO
        SET INS_CODIGO = %s,
            INS_TIPO_INSUMO = %s,
            INS_UNIDAD_MEDIDA = %s,
            INS_COLOR = %s
        WHERE INS_ID = %s
    """
    valores = (codigo, tipo_insumo, unidad_medida, color, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def delInsumo(id):
    sql = "DELETE FROM T_INSUMO WHERE INS_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (id,))
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def searchByCodigo(codigo):
    sql = "SELECT * FROM T_INSUMO WHERE INS_CODIGO = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (codigo,))
    data = c.fetchone()
    c.close()

    if data is None:
        return None

    return Insumo(data[0], data[1], data[2], data[3], data[4], data[5]).to_dic()


def servListInsumoByTipo(tipo_insumo):
    sql = "SELECT * FROM T_INSUMO WHERE INS_TIPO_INSUMO = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (tipo_insumo,))
    data = c.fetchall()
    c.close()

    insumos_l = []
    for i in data:
        insumos_l.append(Insumo(i[0], i[1], i[2], i[3], i[4], i[5]).to_dic())

    return insumos_l