from datetime import date
from Usuario import *
from Articulo import *

# ## PREUBAS USUARIO
usuario1 = Usuario(1, "Juan Pérez", "Calle Falsa 123", "1234567890", "juan@ejemplo.com", "1990-01-01", True, "Ingeniero")

# Actualizar el nombre y el correo
usuario1.actualizar_datos(nombre_completo="Juan David Pérez", correo="juandavidperez@gmail.com")
print(usuario1.__repr__(), "actualizado con exito")

# Crear algunos usuarios
usuario2 = Usuario(2, "Ana García", "Calle Falsa 123", "1234567890", "ana@ejemplo.com", date(1995, 5, 15), True, "Biologa")
usuario3 = Usuario(3, "Pedro López", "Calle Falsa 123", "1234567890", "pedro@ejemplo.com", date(1985, 10, 20), False, estudio="Universidad XYZ")

# Crear una lista de usuarios
nuevos_usuarios = [usuario1, usuario2]

# Crear una colección de usuarios
coleccion = Usuarios()
coleccion.agregar_usuarios(nuevos_usuarios)

# Agregar un usuario individualmente
coleccion.agregar_usuario(usuario3)

# Imprimir todos los usuarios
for usuario in coleccion.usuarios:
    print(usuario.__repr__())