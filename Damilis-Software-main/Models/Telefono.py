class Telefono:
    def __init__(self, id, uuid, user_id, telefono):
        self.TEL_ID        = id
        self.TEL_UUID      = uuid
        self.TEL_USER_ID   = user_id
        self.TEL_TELEFONO  = telefono

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Telefono"""
        return {
            "id"        : self.TEL_ID,
            "uuid"      : self.TEL_UUID,
            "user_id"   : self.TEL_USER_ID,
            "telefono"  : self.TEL_TELEFONO
        }