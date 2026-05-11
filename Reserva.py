# ============================================
# CLASE RESERVA
# ============================================
class Reserva:
   def __init__(self, cliente, servicio, duracion):
       self.cliente = cliente
       self.servicio = servicio
       self.duracion = duracion
       self.estado = "Pendiente"
   def confirmar(self):
       self.estado = "Confirmada"