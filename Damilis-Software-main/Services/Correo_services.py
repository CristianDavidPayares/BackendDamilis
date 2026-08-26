from flask import current_app
from Models.Correo import Correo
import uuid


def servListCorreo():
    sql = "SELECT * FROM T_CORREO"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()

    correos_l = []
    for co in data:
        correos_l.append(Correo(co[0], co[1], co[2], co[3]).to_dic())

    c.close()
    return correos_l


def addCorreo(user_id, correo):
    cor_uuid = str(uuid.uuid4())
    sql = """
        INSERT INTO T_CORREO
        (COR_UUID, COR_USER_ID, COR_CORREO)
        VALUES (%s, %s, %s)
    """
    valores = (cor_uuid, user_id, correo)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    new_id = c.lastrowid
    c.close()

    return Correo(new_id, cor_uuid, user_id, correo).to_dic()


def upCorreo(id, correo):
    sql = "UPDATE T_CORREO SET COR_CORREO = %s WHERE COR_ID = %s"
    valores = (correo, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def delCorreo(id):
    sql = "DELETE FROM T_CORREO WHERE COR_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (id,))
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def servListCorreoByUser(user_id):
    sql = "SELECT * FROM T_CORREO WHERE COR_USER_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (user_id,))
    data = c.fetchall()
    c.close()

    correos_l = []
    for co in data:
        correos_l.append(Correo(co[0], co[1], co[2], co[3]).to_dic())

    return correos_l


def searchByCorreo(correo):
    sql = "SELECT * FROM T_CORREO WHERE COR_CORREO = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (correo,))
    data = c.fetchone()
    c.close()

    if data is None:
        return None

    return Correo(data[0], data[1], data[2], data[3]).to_dic()