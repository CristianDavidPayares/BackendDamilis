class Pqr:
    def __init__(self, id, uuid, descripcion, estado, fecha_respuesta, fecha, cli_id):
        self.PQR_ID                = id
        self.PQR_UUID              = uuid
        self.PQR_DESCRIPCION       = descripcion
        self.PQR_ESTADO            = estado
        self.PQR_FECHA_RESPUESTA   = fecha_respuesta
        self.PQR_FECHA             = fecha
        self.PQR_CLI_ID            = cli_id

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Pqr"""
        return {
            "id"                : self.PQR_ID,
            "uuid"              : self.PQR_UUID,
            "descripcion"       : self.PQR_DESCRIPCION,
            "estado"            : self.PQR_ESTADO,
            "fecha_respuesta"   : self.PQR_FECHA_RESPUESTA,
            "fecha"             : self.PQR_FECHA,
            "cli_id"            : self.PQR_CLI_ID
        }