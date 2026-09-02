from flask import current_app
from Models.Producto import Producto
import uuid


class ProductoService:

    def listar():
        sql = "SELECT * FROM T_PRODUCTO"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        c.close()

        productos_l = []
        for p in data:
            productos_l.append(
                Producto(
                    p[0], p[1], p[2], p[3], p[4], p[5],
                    p[6], p[7], p[8], p[9], p[10]
                ).to_dic()
            )
        return productos_l


    def crear(codigo, talla, color, resena, descripcion, precio, calificacion, imagen, cantidad):
        pro_uuid = str(uuid.uuid4())
        sql = """
            INSERT INTO T_PRODUCTO
            (PRO_UUID, PRO_CODIGO, PRO_TALLA, PRO_COLOR, PRO_RESEÑA,
             PRO_DESCRIPCION, PRO_PRECIO, PRO_CALIFICACION, PRO_IMAGEN, PRO_CANTIDAD)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (pro_uuid, codigo, talla, color, resena, descripcion,
                   precio, calificacion, imagen, cantidad)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        new_id = c.lastrowid
        c.close()

        return Producto(
            new_id, pro_uuid, codigo, talla, color, resena,
            descripcion, precio, calificacion, imagen, cantidad
        ).to_dic()


    def actualizar(id, codigo, talla, color, resena, descripcion, precio, calificacion, imagen, cantidad):
        sql = """
            UPDATE T_PRODUCTO
            SET PRO_CODIGO = %s,
                PRO_TALLA = %s,
                PRO_COLOR = %s,
                PRO_RESENA = %s,
                PRO_DESCRIPCION = %s,
                PRO_PRECIO = %s,
                PRO_CALIFICACION = %s,
                PRO_IMAGEN = %s,
                PRO_CANTIDAD = %s
            WHERE PRO_ID = %s
        """
        valores = (codigo, talla, color, resena, descripcion,
                   precio, calificacion, imagen, cantidad, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_PRODUCTO WHERE PRO_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas


    def buscarPorCodigo(codigo):
        sql = "SELECT * FROM T_PRODUCTO WHERE PRO_CODIGO = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (codigo,))
        data = c.fetchone()
        c.close()

        if data is None:
            return None

        return Producto(
            data[0], data[1], data[2], data[3], data[4], data[5],
            data[6], data[7], data[8], data[9], data[10]
        ).to_dic()


    def actualizarCantidad(id, cantidad):
        sql = "UPDATE T_PRODUCTO SET PRO_CANTIDAD = %s WHERE PRO_ID = %s"
        valores = (cantidad, id)

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()
        filas_afectadas = c.rowcount
        c.close()

        return filas_afectadas