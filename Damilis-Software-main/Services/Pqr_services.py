from flask import current_app
from Models.Pqr import Pqr
from datetime import datetime
import uuid


def servListPqr():
    sql = "SELECT * FROM T_PQR"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()

    pqrs_l = []
    for p in data:
        pqrs_l.append(Pqr(p[0], p[1], p[2], p[3], p[4], p[5], p[6]).to_dic())

    c.close()
    return pqrs_l


def addPqr(descripcion, cli_id):
    pqr_uuid = str(uuid.uuid4())
    fecha = datetime.now()
    estado = "PENDIENTE"

    sql = """
        INSERT INTO T_PQR
        (PQR_UUID, PQR_DESCRIPCION, PQR_ESTADO, PQR_FECHA_RESPUESTA, PQR_FECHA, PQR_CLI_ID)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (pqr_uuid, descripcion, estado, None, fecha, cli_id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    new_id = c.lastrowid
    c.close()

    return Pqr(new_id, pqr_uuid, descripcion, estado, None, fecha, cli_id).to_dic()


def upPqr(id, descripcion):
    sql = "UPDATE T_PQR SET PQR_DESCRIPCION = %s WHERE PQR_ID = %s"
    valores = (descripcion, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def delPqr(id):
    sql = "DELETE FROM T_PQR WHERE PQR_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (id,))
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def servListPqrByCliente(cli_id):
    sql = "SELECT * FROM T_PQR WHERE PQR_CLI_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (cli_id,))
    data = c.fetchall()
    c.close()

    pqrs_l = []
    for p in data:
        pqrs_l.append(Pqr(p[0], p[1], p[2], p[3], p[4], p[5], p[6]).to_dic())

    return pqrs_l


def responderPqr(id, estado):
    fecha_respuesta = datetime.now()
    sql = "UPDATE T_PQR SET PQR_ESTADO = %s, PQR_FECHA_RESPUESTA = %s WHERE PQR_ID = %s"
    valores = (estado, fecha_respuesta, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas