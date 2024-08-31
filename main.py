from Usuario import Usuario
from Articulo import *

## PREUBAS USUARIO
usuario1 = Usuario(1, "Juan Pérez", "Calle Falsa 123", "1234567890", "juan@ejemplo.com", "1990-01-01", True, "Ingeniero")

# Intentar crear un usuario con un correo inválido
try:
    usuario_invalido = Usuario(2, "María López", "Avenida Principal 456", "9876543210", "mariagmail.com.co", "1995-05-15", False, estudio="Universidad XYZ")
except ValueError as e:
    print(e)
if usuario1 != None:
        print(f"Usuario {usuario1.nombre_completo} creado con exito")