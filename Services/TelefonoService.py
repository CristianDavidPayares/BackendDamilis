from flask import current_app
from Models.Telefono import Telefono
import uuid


class TelefonoService:

    @staticmethod
    def listar():
        sql = "SELECT * FROM T_TELEFONO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        telefonos_l = []
        for t in data:
            telefonos_l.append(
                Telefono(t[0], t[1], t[2], t[3]).to_dic()
            )
        return telefonos_l


    @staticmethod
    def crear(user_id, telefono):
        tel_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_TELEFONO
            (TEL_UUID, TEL_USER_ID, TEL_TELEFONO)
            VALUES (%s, %s, %s)
        """
        valores = (tel_uuid, user_id, telefono)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return Telefono(new_id, tel_uuid, user_id, telefono).to_dic()


    @staticmethod
    def actualizar(id, telefono):
        sql = "UPDATE T_TELEFONO SET TEL_TELEFONO = %s WHERE TEL_ID = %s"
        valores = (telefono, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    @staticmethod
    def eliminar(id):
        sql = "DELETE FROM T_TELEFONO WHERE TEL_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    @staticmethod
    def listarPorUsuario(user_id):
        sql = "SELECT * FROM T_TELEFONO WHERE TEL_USER_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (user_id,))
        data = c.fetchall()
        c.close()

        telefonos_l = []
        for t in data:
            telefonos_l.append(
                Telefono(t[0], t[1], t[2], t[3]).to_dic()
            )
        return telefonos_l