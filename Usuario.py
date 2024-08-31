import re

class Usuario:
    def __init__(self, cc, nombre_completo, direccion, celular, correo, fecha_nacimiento, trabaja, cargo=None, estudio=None):
        self.id = cc
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
        regex = r".*@.*"
        if not re.fullmatch(regex, correo):
            raise ValueError("Correo electrónico inválido")
        return correo

    def _validar_celular(self, celular):
        # Valida si el celular es un número
        if not celular.isdigit():
            raise ValueError("Número de celular inválido")
        return celular
    
    def actualizar_datos(self, **kwargs):
        #crea un diccionario que mira los valores existentes
        #Raises ValueError: Si se intenta actualizar un atributo que no existe o si el valor proporcionado no es válido.
        for atributo, nuevo_valor in kwargs.items():
            if hasattr(self, atributo):
                if atributo in ["celular", "correo"]:
                    # Validar los valores nuevamente si se modifican
                    nuevo_valor = getattr(self, f"_validar_{atributo}")(nuevo_valor)
                setattr(self, atributo, nuevo_valor)
            else:
                raise ValueError(f"El atributo '{atributo}' no existe en la clase Usuario.")
            
    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre_completo}', correo='{self.correo}')"
    
class Usuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_usuarios(self, lista_usuarios):
        """Agrega una lista de usuarios a la colección."""
        self.usuarios.extend(lista_usuarios)