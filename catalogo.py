class Catalogo:
    def __init__(self):
        self.articulos = {}  # Diccionario para almacenar los artículos por ID

    def agregar_articulo(self, articulo):
        self.articulos[articulo.id] = articulo

    def buscar_articulo(self, criterio):
        # Búsqueda por ID o por parte del título
        resultados = []
        for articulo in self.articulos.values():
            if str(articulo.id) == criterio or criterio in articulo.titulo:
                resultados.append(articulo)
        return resultados

    def validar_disponibilidad(self, articulo_id):
        articulo = self.articulos.get(articulo_id)
        if articulo and articulo.estado == "Disponible":
            return True
        return False

    def notificar_pendiente(self, usuarios, mensaje):
        usuarios_notificados = []
        for usuario in usuarios:
            print(f"Notificación enviada a {usuario.correo}: {mensaje}")
            usuarios_notificados.append(usuario)
        return usuarios_notificados

    def reservar(self, articulo_id, usuario, fecha_reserva):
        articulo = self.articulos.get(articulo_id)
        if articulo and articulo.estado == "Disponible":
            articulo.estado = "Reservado"
            # Agregar lógica para almacenar la reserva (e.g., en una lista de reservas)
            print(f"Artículo {articulo.titulo} reservado para {usuario.nombre} hasta {fecha_reserva}")
        else:
            print("Artículo no disponible para reserva.")


    