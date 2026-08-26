from flask import current_app
from Models.admin import Admin
import uuid


def servListAdmin():
    sql = "SELECT * FROM T_ADMIN"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()

    admins_l = []
    for a in data:
        admins_l.append(Admin(a[0], a[1], a[2], a[3], a[4]).to_dic())

    c.close()
    return admins_l


def addAdmin(actual_catalogo, observaciones, user_id):
    adm_uuid = str(uuid.uuid4())
    sql = """
        INSERT INTO T_ADMIN
        (ADM_UUID, ADM_ACTUAL_CATLOGO, ADM_OBSERVACIONES, ADM_USER_ID)
        VALUES (%s, %s, %s, %s)
    """
    valores = (adm_uuid, actual_catalogo, observaciones, user_id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    new_id = c.lastrowid
    c.close()

    return Admin(new_id, adm_uuid, actual_catalogo, observaciones, user_id).to_dic()


def upAdmin(id, actual_catalogo, observaciones):
    sql = """
        UPDATE T_ADMIN
        SET ADM_ACTUAL_CATLOGO = %s,
            ADM_OBSERVACIONES = %s
        WHERE ADM_ID = %s
    """
    valores = (actual_catalogo, observaciones, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def delAdmin(id):
    sql = "DELETE FROM T_ADMIN WHERE ADM_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (id,))
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def searchByUserId(user_id):
    sql = "SELECT * FROM T_ADMIN WHERE ADM_USER_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (user_id,))
    data = c.fetchone()
    c.close()

    if data is None:
        return None

    return Admin(data[0], data[1], data[2], data[3], data[4]).to_dic()