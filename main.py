from datetime import datetime

class Usuario:
    def __init__(self, cc, nombre_completo, direccion, celular, correo, fecha_nacimiento, articulos_pendientes = 0):
        self.cc = cc
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.celular = celular
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento