class Articulo:
    def __init__(self, id, titulo, autor, estado="Disponible"):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

class Articulo_Factory:
    #kwargs es la forma de pasar multiples argumentos a una función
    def crear_articulo(self, tipo, **kwargs):
        if tipo == "libro":
            return Libro(**kwargs)
        elif tipo == "revista":
            return Revista(**kwargs)
        elif tipo == "periodico":
            return Periodico(**kwargs)
        elif tipo == "cd":
            return CD(**kwargs)
        elif tipo == "dvd":
            return DVD(**kwargs)
        else:
            raise ValueError("Tipo de artículo no válido")

class Libro(Articulo):
    def __init__(self, id, titulo, autor, isbn, editorial, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.isbn = isbn
        self.editorial = editorial

    def __repr__(self):
        return f"Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', isbn='{self.isbn}', editorial='{self.editorial}')"

class Revista(Articulo):
    def __init__(self, id, titulo, autor, issn, periodicidad, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.issn = issn
        self.periodicidad = periodicidad

    def __repr__(self):
        return f"Revista(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', issn='{self.issn}', periodicidad='{self.periodicidad}')"

class Periodico(Articulo):
    def __init__(self, id, titulo, autor, fecha_publicacion, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.fecha_publicacion = fecha_publicacion

    def __repr__(self):
        return f"Periodico(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', fecha_publicacion='{self.fecha_publicacion}')"

class CD(Articulo):
    def __init__(self, id, titulo, autor, genero, formato, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.genero = genero
        self.formato = formato

    def __repr__(self):
        return f"CD(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', genero='{self.genero}', formato='{self.formato}')"

class DVD(Articulo):
    def __init__(self, id, titulo, autor, genero, duracion, **kwargs):
        super().__init__(id, titulo, autor, **kwargs)
        self.genero = genero
        self.duracion = duracion

    def __repr__(self):
        return f"DVD(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', genero='{self.genero}', duracion='{self.duracion}')"
