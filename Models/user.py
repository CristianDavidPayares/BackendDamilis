class Usuario:
    def __init__(self, id, cedula, uuid, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
        self.USER_ID                 = id
        self.USER_CEDULA             = cedula
        self.USER_UUID               = uuid
        self.USER_PRIMER_NOMBRE      = primer_nombre
        self.USER_SEGUNDO_NOMBRE     = segundo_nombre
        self.USER_PRIMER_APELLIDO    = primer_apellido
        self.USER_SEGUNDO_APELLIDO   = segundo_apellido

    def to_dic(self):
        """retorna un diccionario con los atributos de la clase Usuario"""
        return {
            "id"                : self.USER_ID,
            "cedula"            : self.USER_CEDULA,
            "uuid"              : self.USER_UUID,
            "primer_nombre"     : self.USER_PRIMER_NOMBRE,
            "segundo_nombre"    : self.USER_SEGUNDO_NOMBRE,
            "primer_apellido"   : self.USER_PRIMER_APELLIDO,
            "segundo_apellido"  : self.USER_SEGUNDO_APELLIDO
        }