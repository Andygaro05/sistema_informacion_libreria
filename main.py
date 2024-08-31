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

##Pruebas articulo
factory = Articulo_Factory()
libro1 = factory.crear_articulo("libro", id=1, titulo="Don Quijote", autor="Cervantes", isbn="1234567890", editorial="Planeta")
revista1 = factory.crear_articulo("revista", id=2, titulo="National Geographic", autor="Varios", issn="1234-5678", periodicidad="Mensual")
cd1 = factory.crear_articulo("cd", id=3, titulo="Thriller", autor="Michael Jackson", genero="Pop", formato="CD-Audio")

#ajustar para que muestre los valores del print no las direcciones de memoria
print(libro1)
print(revista1)
print(cd1)