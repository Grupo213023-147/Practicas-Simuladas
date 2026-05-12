# ============================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Clase Servicio del sistema
# Autor: KAROL YULIANA VARGAS RIZO
#
# Funciones principales:
# - Registro de servicios
# - Clasificación de servicios por categoría
# - Gestión de precios
# - Visualización de detalles del servicio
# ============================================================
class Reserva:

   def _init_(self, cliente, servicio, duracion):
       self.cliente = cliente
       self.servicio = servicio
       self.duracion = duracion
       self.estado = "Pendiente"

   def confirmar(self):
       self.estado = "Confirmada"
