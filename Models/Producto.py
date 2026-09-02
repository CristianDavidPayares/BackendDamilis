class Producto:
    def __init__(self, id, uuid, codigo, talla, color, resena, descripcion, precio, calificacion, imagen, cantidad):
        self.PRO_ID             = id
        self.PRO_UUID           = uuid
        self.PRO_CODIGO         = codigo
        self.PRO_TALLA          = talla
        self.PRO_COLOR          = color
        self.PRO_RESENA         = resena
        self.PRO_DESCRIPCION    = descripcion
        self.PRO_PRECIO         = precio
        self.PRO_CALIFICACION   = calificacion
        self.PRO_IMAGEN         = imagen
        self.PRO_CANTIDAD       = cantidad

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Producto"""
        return {
            "id"            : self.PRO_ID,
            "uuid"          : self.PRO_UUID,
            "codigo"        : self.PRO_CODIGO,
            "talla"         : self.PRO_TALLA,
            "color"         : self.PRO_COLOR,
            "resena"        : self.PRO_RESENA,
            "descripcion"   : self.PRO_DESCRIPCION,
            "precio"        : self.PRO_PRECIO,
            "calificacion"  : self.PRO_CALIFICACION,
            "imagen"        : self.PRO_IMAGEN,
            "cantidad"      : self.PRO_CANTIDAD
        }