# ============================================
# CLASES SERVICIOS
# ============================================
class Servicio:
   def __init__(self, nombre, precio):
       self.nombre = nombre
       self.precio = precio
   def descripcion(self):
       return f"{self.nombre} - ${self.precio:.2f}"

class ServicioSala(Servicio):
   pass

class ServicioEquipo(Servicio):
   pass

class ServicioAsesoria(Servicio):
   pass