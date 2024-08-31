from datetime import datetime

import re

class Usuario:
    def __init__(self, id, nombre_completo, direccion, celular, correo, fecha_nacimiento, trabaja, cargo=None, estudio=None):
        self.id = id
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.celular = self._validar_celular(celular)
        self.correo = self._validar_correo(correo)
        self.fecha_nacimiento = fecha_nacimiento
        self.trabaja = trabaja
        self.cargo = cargo
        self.estudio = estudio

    def _validar_correo(self, correo):
        # Expresión regular básica para validar correos electrónicos
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, correo):
            raise ValueError("Correo electrónico inválido")
        return correo

    def _validar_celular(self, celular):
        # Valida si el celular es un número
        if not celular.isdigit():
            raise ValueError("Número de celular inválido")
        return celular