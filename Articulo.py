class Articulo:
    def __init__(self, id, titulo, autor, estado="Disponible", categoria="Otro"):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.estado = estado  # Disponible, Prestado, Perdido, Dañado
        self.categoria = categoria  # Libro, Revista, DVD, etc.

#añadir el factory cuando funcione c/u
class Libro(Articulo):
    def __init__(self, id, titulo, autor, isbn, editorial, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.isbn = isbn
        self.editorial = editorial

class Revista(Articulo):
    def __init__(self, id, titulo, autor, issn, periodicidad, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.issn = issn
        self.periodicidad = periodicidad

class Periodico(Articulo):
    def __init__(self, id, titulo, autor, fecha_publicacion, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.fecha_publicacion = fecha_publicacion

class CD(Articulo):
    def __init__(self, id, titulo, autor, genero, formato, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.genero = genero
        self.formato = formato

class DVD(Articulo):
    def __init__(self, id, titulo, autor, genero, duracion, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.genero = genero
        self.duracion = duracion
