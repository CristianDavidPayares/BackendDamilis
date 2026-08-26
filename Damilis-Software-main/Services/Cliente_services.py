from flask import current_app
from Models.Cliente import Cliente
from datetime import datetime
import uuid


def servListCliente():
    sql = "SELECT * FROM T_CLIENTE"
    c = current_app.mysql.connection.cursor()
    c.execute(sql)
    data = c.fetchall()

    clientes_l = []
    for cl in data:
        clientes_l.append(Cliente(cl[0], cl[1], cl[2], cl[3], cl[4], cl[5], cl[6], cl[7]).to_dic())

    c.close()
    return clientes_l


def addCliente(preferencias, per_cedula, user_id):
    cli_uuid = str(uuid.uuid4())
    fecha_registro = datetime.now()
    estado = "ACTIVO"

    sql = """
        INSERT INTO T_CLIENTE
        (CLI_UUID, CLI_ESTADO, CLI_PREFERENCIAS, CLI_FECHA_REGISTRO, CLI_PER_CEDULA, CLI_PQR_ID, CLI_USER_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (cli_uuid, estado, preferencias, fecha_registro, per_cedula, None, user_id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    new_id = c.lastrowid
    c.close()

    return Cliente(new_id, cli_uuid, estado, preferencias, fecha_registro, per_cedula, None, user_id).to_dic()


def upCliente(id, preferencias):
    sql = "UPDATE T_CLIENTE SET CLI_PREFERENCIAS = %s WHERE CLI_ID = %s"
    valores = (preferencias, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def delCliente(id):
    sql = "DELETE FROM T_CLIENTE WHERE CLI_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (id,))
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def cambiarEstado(id, estado):
    sql = "UPDATE T_CLIENTE SET CLI_ESTADO = %s WHERE CLI_ID = %s"
    valores = (estado, id)

    c = current_app.mysql.connection.cursor()
    c.execute(sql, valores)
    current_app.mysql.connection.commit()
    filas_afectadas = c.rowcount
    c.close()

    return filas_afectadas


def searchByCedula(per_cedula):
    sql = "SELECT * FROM T_CLIENTE WHERE CLI_PER_CEDULA = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (per_cedula,))
    data = c.fetchone()
    c.close()

    if data is None:
        return None

    return Cliente(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]).to_dic()


def searchByUserId(user_id):
    sql = "SELECT * FROM T_CLIENTE WHERE CLI_USER_ID = %s"

    c = current_app.mysql.connection.cursor()
    c.execute(sql, (user_id,))
    data = c.fetchone()
    c.close()

    if data is None:
        return None

    return Cliente(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]).to_dic()