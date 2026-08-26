class Direccion:
    def __init__(self, id, uuid, user_id, direccion):
        self.DIR_ID          = id
        self.DIR_UUID        = uuid
        self.DIR_USER_ID     = user_id
        self.DIR_DIRECCION   = direccion

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Direccion"""
        return {
            "id"          : self.DIR_ID,
            "uuid"        : self.DIR_UUID,
            "user_id"     : self.DIR_USER_ID,
            "direccion"   : self.DIR_DIRECCION
        }