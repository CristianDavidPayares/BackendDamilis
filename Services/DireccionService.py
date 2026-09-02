from flask import current_app
from Models.Direccion import Direccion
import uuid

class DireccionService:

    
    def listar():
        sql = "SELECT * FROM T_DIRECCION"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()
        direcciones_l = []
        for d in data:
            direcciones_l.append(Direccion(d[0], d[1], d[2], d[3]).to_dic())
        return direcciones_l

    
    def crear(user_id, direccion):
        dir_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_DIRECCION
            (DIR_UUID, DIR_USER_ID, DIR_DIRECCION)
            VALUES (%s, %s, %s)
        """
        valores = (dir_uuid, user_id, direccion)
        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()
        return Direccion(new_id, dir_uuid, user_id, direccion).to_dic()

    
    def actualizar(id, direccion):
        sql = "UPDATE T_DIRECCION SET DIR_DIRECCION = %s WHERE DIR_ID = %s"
        valores = (direccion, id)
        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        return filas_afectadas

    
    def eliminar(id):
        sql = "DELETE FROM T_DIRECCION WHERE DIR_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()
        return filas_afectadas

    
    def listarPorUsuario(user_id):
        sql = "SELECT * FROM T_DIRECCION WHERE DIR_USER_ID = %s"
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (user_id,))
        data = c.fetchall()
        c.close()
        direcciones_l = []
        for d in data:
            direcciones_l.append(Direccion(d[0], d[1], d[2], d[3]).to_dic())
        return direcciones_l