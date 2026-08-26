class Correo:
    def __init__(self, id, uuid, user_id, correo):
        self.COR_ID       = id
        self.COR_UUID     = uuid
        self.COR_USER_ID  = user_id
        self.COR_CORREO   = correo

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Correo"""
        return {
            "id"        : self.COR_ID,
            "uuid"      : self.COR_UUID,
            "user_id"   : self.COR_USER_ID,
            "correo"    : self.COR_CORREO
        }