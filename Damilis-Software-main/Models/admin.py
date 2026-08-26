class Admin:
    def __init__(self, id, uuid, actual_catalogo, observaciones, user_id):
        self.ADM_ID              = id
        self.ADM_UUID            = uuid
        self.ADM_ACTUAL_CATLOGO  = actual_catalogo
        self.ADM_OBSERVACIONES   = observaciones
        self.ADM_USER_ID         = user_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Admin"""
        return {
            "id"             : self.ADM_ID,
            "uuid"           : self.ADM_UUID,
            "actual_catalogo": self.ADM_ACTUAL_CATLOGO,
            "observaciones"  : self.ADM_OBSERVACIONES,
            "user_id"        : self.ADM_USER_ID
        }