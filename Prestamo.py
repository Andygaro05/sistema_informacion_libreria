from Usuario import *
from Articulo import Articulo
from Catalogo import Catalogo
import datetime

class Prestamo:
  def __init__(self, usuario, articulo, fecha_prestamo, fecha_devolucion=None, multa=0):
      self.usuario = usuario
      self.articulo = articulo
      self.fecha_prestamo = fecha_prestamo
      self.fecha_devolucion = fecha_devolucion
      self.multa = multa
      self.estado = "En curso"  # Estados posibles: "En curso", "Devuelto", "Perdido", "Dañado"
    
  def realizar_prestamo(self, usuario_id, criterio):
    usuario = Usuarios.buscar_usuario(self,cc=usuario_id)
    articulo = Catalogo.buscar_articulo(criterio)

    if usuario and articulo and articulo.estado == "Disponible":
        self.prestamos.append((usuario, articulo))
        articulo.estado = "Prestado"
        return True
    return False

  def realizar_reserva(self, usuario_id, articulo_id, fecha_reserva):
    usuario = self.usuario(usuario_id)
    articulo = self.catalogo.buscar_articulo(articulo_id)
    if usuario and articulo and self.catalogo.validar_disponibilidad(articulo_id):
        self.catalogo.reservar(articulo_id, usuario, fecha_reserva)
        self.reservas.append((usuario, articulo, fecha_reserva))
        return True
    return False

  def devolver_articulo(self, fecha_prestamo, fecha_devolucion=datetime.date.today()):
    self.fecha_devolucion = fecha_devolucion
    self.estado = "Devuelto"
    self.calcular_multa(fecha_prestamo, fecha_devolucion=datetime.date.today())

  def calcular_multa(self, fecha_prestamo, fecha_devolucion):
    dias =  fecha_devolucion - fecha_prestamo
    limite = 15
    multa_dia = 1000
    if dias > limite:
      multa = dias * multa_dia
    else:
      multa = 0
    return multa

  def __str__(self):
    return f"Préstamo: Usuario={self.usuario.nombre}, Artículo={self.articulo.titulo}, Fecha de Préstamo={self.fecha_prestamo}, Fecha de Devolución={self.fecha_devolucion}, Multa={self.multa}, Estado={self.estado}"