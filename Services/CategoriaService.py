from flask import current_app
from Models.Categoria import Categoria
import uuid

class CategoriaService:

    def listar():
        sql = "SELECT * FROM T_CATEGORIA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()

        categorias_l = []
        for ca in data:
            categorias_l.append(Categoria(ca[0], ca[1], ca[2]).to_dic())

        c.close()
        return categorias_l


    def crear(tipo_categoria):
        cat_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_CATEGORIA
            (CAT_UUID, CAT_TIPO_CATEGORIA)
            VALUES (%s, %s)
        """
        valores = (cat_uuid, tipo_categoria)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return Categoria(new_id, cat_uuid, tipo_categoria).to_dic()


    def actualizar(id, tipo_categoria):
        sql = "UPDATE T_CATEGORIA SET CAT_TIPO_CATEGORIA = %s WHERE CAT_ID = %s"
        valores = (tipo_categoria, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_CATEGORIA WHERE CAT_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def buscarPorTipo(tipo_categoria):
        sql = "SELECT * FROM T_CATEGORIA WHERE CAT_TIPO_CATEGORIA = %s"
    
        c = current_app.mysql.connection.cursor()
        c.execute(sql, (tipo_categoria,))
        data = c.fetchone()
        c.close()

        if data is None:
            return None

        return Categoria(data[0], data[1], data[2]).to_dic()