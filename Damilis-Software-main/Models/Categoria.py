class Categoria:
    def __init__(self, id, uuid, tipo_categoria):
        self.CAT_ID              = id
        self.CAT_UUID            = uuid
        self.CAT_TIPO_CATEGORIA  = tipo_categoria

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Categoria"""
        return {
            "id"              : self.CAT_ID,
            "uuid"            : self.CAT_UUID,
            "tipo_categoria"  : self.CAT_TIPO_CATEGORIA
        }