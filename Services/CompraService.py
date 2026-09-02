from flask import current_app
from Models.Compra import Compra
from datetime import datetime
import uuid


class CompraService:

    def listar():
        sql = "SELECT * FROM T_COMPRA"

        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()

        compras_l = []

        for co in data:
            compras_l.append(
                Compra(
                    co[0],
                    co[1],
                    co[2],
                    co[3],
                    co[4],
                    co[5],
                    co[6]
                ).to_dic()
            )

        c.close()
        return compras_l


    def crear(subtotal, metodo_pago, numero_compras, cli_id):
        comp_uuid = str(uuid.uuid4())
        fecha_compra = datetime.now()

        sql = """
            INSERT INTO T_COMPRA
            (
                COMP_UUID,
                COMP_FECHA_COMPRA,
                COMP_SUBTOTAL,
                COMP_METODO_PAGO,
                COMP_NUMERO_COMPRAS,
                COMP_CLI_ID
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            comp_uuid,
            fecha_compra,
            subtotal,
            metodo_pago,
            numero_compras,
            cli_id
        )

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        new_id = c.lastrowid

        c.close()

        return Compra(
            new_id,
            comp_uuid,
            fecha_compra,
            subtotal,
            metodo_pago,
            numero_compras,
            cli_id
        ).to_dic()


    def actualizar(id, subtotal, metodo_pago, numero_compras):
        sql = """
            UPDATE T_COMPRA
            SET COMP_SUBTOTAL = %s,
                COMP_METODO_PAGO = %s,
                COMP_NUMERO_COMPRAS = %s
            WHERE COMP_ID = %s
        """

        valores = (
            subtotal,
            metodo_pago,
            numero_compras,
            id
        )

        c = current_app.mysql.connection.cursor()
        c.execute(sql, valores)
        current_app.mysql.connection.commit()

        filas_afectadas = c.rowcount

        c.close()

        return filas_afectadas


    def eliminar(id):
        sql = "DELETE FROM T_COMPRA WHERE COMP_ID = %s"

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (id,))
        current_app.mysql.connection.commit()

        filas_afectadas = c.rowcount

        c.close()

        return filas_afectadas


    def listarPorCliente(cli_id):
        sql = """
            SELECT * FROM T_COMPRA
            WHERE COMP_CLI_ID = %s
            ORDER BY COMP_FECHA_COMPRA DESC
        """

        c = current_app.mysql.connection.cursor()
        c.execute(sql, (cli_id,))
        data = c.fetchall()

        c.close()

        compras_l = []

        for co in data:
            compras_l.append(
                Compra(
                    co[0],
                    co[1],
                    co[2],
                    co[3],
                    co[4],
                    co[5],
                    co[6]
                ).to_dic()
            )

        return compras_l