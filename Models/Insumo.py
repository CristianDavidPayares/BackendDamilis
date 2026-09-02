class Insumo:
    def __init__(self, id, uuid, codigo, tipo_insumo, unidad_medida, color):
        self.INS_ID             = id
        self.INS_UUID           = uuid
        self.INS_CODIGO         = codigo
        self.INS_TIPO_INSUMO    = tipo_insumo
        self.INS_UNIDAD_MEDIDA  = unidad_medida
        self.INS_COLOR          = color

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Insumo"""
        return {
            "id"             : self.INS_ID,
            "uuid"           : self.INS_UUID,
            "codigo"         : self.INS_CODIGO,
            "tipo_insumo"    : self.INS_TIPO_INSUMO,
            "unidad_medida"  : self.INS_UNIDAD_MEDIDA,
            "color"          : self.INS_COLOR
        }