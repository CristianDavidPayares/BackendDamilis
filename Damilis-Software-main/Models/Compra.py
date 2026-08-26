class Compra:
    def __init__(self, id, uuid, fecha_compra, subtotal, metodo_pago, numero_compras, cli_id):
        self.COMP_ID              = id
        self.COMP_UUID            = uuid
        self.COMP_FECHA_COMPRA    = fecha_compra
        self.COMP_SUBTOTAL        = subtotal
        self.COMP_METODO_PAGO     = metodo_pago
        self.COMP_NUMERO_COMPRAS  = numero_compras
        self.COMP_CLI_ID          = cli_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Compra"""
        return {
            "id"               : self.COMP_ID,
            "uuid"             : self.COMP_UUID,
            "fecha_compra"     : self.COMP_FECHA_COMPRA,
            "subtotal"         : self.COMP_SUBTOTAL,
            "metodo_pago"      : self.COMP_METODO_PAGO,
            "numero_compras"   : self.COMP_NUMERO_COMPRAS,
            "cli_id"           : self.COMP_CLI_ID
        }