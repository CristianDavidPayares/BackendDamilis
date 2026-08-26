from flask import current_app
from Models.user import Usuario
import uuid


def servListUser():
    sql = "SELECT * FROM T_USUARIO"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()

    users_l = []
    for u in data:
        users_l.append(Usuario(u[0], u[1], u[2], u[3], u[4], u[5], u[6]).to_dic())

    c.close()
    return users_l


def addUser(cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    us_uuid = str(uuid.uuid4())
    sql = """
        INSERT INTO T_USUARIO
        (USER_CEDULA, USER_UUID, USER_PRIMER_NOMBRE, USER_SEGUNDO_NOMBRE, USER_PRIMER_APELLIDO, USER_SEGUNDO_APELLIDO)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (cedula, us_uuid, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    new_id = c.lastrowid
    c.close()

    return Usuario(new_id, cedula, us_uuid, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido).to_dic()


def upUser(id, cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    sql = """
        UPDATE T_USUARIO
        SET USER_CEDULA = %s,
            USER_PRIMER_NOMBRE = %s,
            USER_SEGUNDO_NOMBRE = %s,
            USER_PRIMER_APELLIDO = %s,
            USER_SEGUNDO_APELLIDO = %s
        WHERE USER_ID = %s
    """
    valores = (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def delUser(id):

    sql = "DELETE FROM T_USUARIO WHERE USER_ID = %s"

    c = current_app.mysql.connection.cursor()

    c.execute(sql, (id,))

    current_app.mysql.connection.commit()

    filas_afectadas = c.rowcount

    c.close()

    return filas_afectadas


def searchByDoc(cedula):
    sql = "SELECT * FROM T_USUARIO WHERE USER_CEDULA = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (cedula,))
    data = c.fetchone()
    c.close()

    if data is None:
        return None

    return Usuario(data[0], data[1], data[2], data[3], data[4], data[5], data[6]).to_dic()
