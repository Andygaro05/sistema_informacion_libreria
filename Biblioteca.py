import pandas as pd
from Catalogo import Catalogo
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = Catalogo()  # Instancia de la clase Catalogo
        self.usuarios = {}  # Diccionario para almacenar los usuarios por ID
        self.prestamos = []  # Lista para almacenar los préstamos
        self.reservas = []  # Lista para almacenar las reservas

    def agregar_articulo(self, articulo):
        self.catalogo.agregar_articulo(articulo)

    def agregar_usuario(self, usuario):
        self.usuarios[usuario.id] = usuario

    def realizar_prestamo(self, usuario_id, articulo_id):
        usuario = self.usuarios.get(usuario_id)
        articulo = self.catalogo.buscar_articulo(articulo_id)
        if usuario and articulo and self.catalogo.validar_disponibilidad(articulo_id):
            self.prestamos.append((usuario, articulo))
            articulo.estado = "Prestado"
            return True
        return False

    def realizar_reserva(self, usuario_id, articulo_id, fecha_reserva):
        usuario = self.usuarios.get(usuario_id)
        articulo = self.catalogo.buscar_articulo(articulo_id)
        if usuario and articulo and self.catalogo.validar_disponibilidad(articulo_id):
            self.catalogo.reservar(articulo_id, usuario, fecha_reserva)
            self.reservas.append((usuario, articulo, fecha_reserva))
            return True
        return False

    # def devolver_articulo(self, usuario_id, articulo_id):
    #     # ... Implementación para devolver un artículo

    def generar_reporte(self):
        # Calcular métricas:
        articulos_mas_prestados = sorted(self.catalogo.values(), key=lambda x: x.veces_prestado, reverse=True)
        usuarios_mas_activos = sorted(self.usuarios.values(), key=lambda x: len(x.prestamos), reverse=True)
        # ... Calcular artículos perdidos/dañados y multas (implementar lógica)
        # Crear un DataFrame de pandas con los datos del reporte
        data = {
            'Artículo': [articulo.titulo for articulo in articulos_mas_prestados],
            'Veces Prestado': [articulo.veces_prestado for articulo in articulos_mas_prestados],
            'Usuario': [usuario.nombre for usuario in usuarios_mas_activos],
            'Préstamos': [len(usuario.prestamos) for usuario in usuarios_mas_activos],
            # ... Agregar columnas para perdidos, dañados, multas
        }
        df = pd.DataFrame(data)
        return df

    def exportar_excel(self, ruta_archivo):
        df = self.generar_reporte()
        df.to_excel(ruta_archivo, index=False)

