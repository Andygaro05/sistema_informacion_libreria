class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        for u in self.usuarios:
            if u == usuario:
                u.prestar_libro(libro)
                return
        print("Usuario no encontrado.")

