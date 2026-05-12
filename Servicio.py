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
class Cliente:

   def _init_(self, nombre, identificacion):
       self.nombre = nombre
       self.identificacion = identificacion

   def get_nombre(self):
       return self.nombre
