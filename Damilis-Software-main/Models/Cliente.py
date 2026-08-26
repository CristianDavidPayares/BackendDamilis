class Cliente:
    def __init__(self, id, uuid, estado, preferencias, fecha_registro, per_cedula, pqr_id, user_id):
        self.CLI_ID               = id
        self.CLI_UUID             = uuid
        self.CLI_ESTADO           = estado
        self.CLI_PREFERENCIAS     = preferencias
        self.CLI_FECHA_REGISTRO   = fecha_registro
        self.CLI_PER_CEDULA       = per_cedula
        self.CLI_PQR_ID           = pqr_id
        self.CLI_USER_ID          = user_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Cliente"""
        return {
            "id"             : self.CLI_ID,
            "uuid"           : self.CLI_UUID,
            "estado"         : self.CLI_ESTADO,
            "preferencias"   : self.CLI_PREFERENCIAS,
            "fecha_registro" : self.CLI_FECHA_REGISTRO,
            "per_cedula"     : self.CLI_PER_CEDULA,
            "pqr_id"         : self.CLI_PQR_ID,
            "user_id"        : self.CLI_USER_ID
        }