from datetime import date
from usuario import *
from articulo import *
from biblioteca import *
from catalogo import *
from prestamo import *


biblioteca = Biblioteca("Alejandria")
usuario1 = Usuario(1, "Juan Pérez", "Calle Falsa 123", "1234567890", "juan@ejemplo.com", "1990-01-01", True, "Ingeniero")

# Actualizar el nombre y el correo
usuario1.actualizar_datos(nombre_completo="Juan David Pérez", correo="juandavidperez@gmail.com")
print(usuario1.__repr__(), "actualizado con exito")

# Crear algunos usuarios
usuario2 = Usuario(2, "Ana García", "Calle Falsa 123", "1234567890", "ana@ejemplo.com", date(1995, 5, 15), True, "Biologa")
usuario3 = Usuario(3, "Pedro López", "Calle Falsa 123", "1234567890", "pedro@ejemplo.com", date(1985, 10, 20), False, estudio="Universidad XYZ")
nuevos_usuarios = [usuario1, usuario2]

libro1 = Libro(1, "El Quijote", "Miguel de Cervantes", "978-84-206-6223-2", "Editorial Planeta")
revista1 = Revista(2, "National Geographic", "Varios autores", "0027-8357", "Mensual")
cd1 = CD(3, "Thriller", "Michael Jackson", "Pop", "CD")

coleccion = Usuarios()
coleccion.agregar_usuarios(nuevos_usuarios)
coleccion.agregar_usuario(usuario3)

catalogo = Catalogo()
catalogo.agregar_articulo(libro1)
catalogo.agregar_articulo(revista1)
catalogo.agregar_articulo(cd1)

usuarios = Usuarios()
usuarios.agregar_usuario(usuario1)
usuarios.agregar_usuario(usuario2)
usuarios.agregar_usuario(usuario3)

# Buscar artículos por parte del título
resultados = catalogo.buscar_articulo("National")
for articulo in resultados:
    print(articulo)
    
# prestamo = Prestamo(usuario1, libro1, date.today())
# prestamo.realizar_prestamo(usuario1.id, "El Quijote")

if prestamo:
    print("Préstamo realizado con éxito.")
else:
    print("No se pudo realizar el préstamo.")