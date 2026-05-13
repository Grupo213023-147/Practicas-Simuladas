# ============================================
# CLASE CLIENTE
# ============================================
# Esta clase representa a un cliente con su nombre e identificacion

class Cliente:
   def __init__(self, nombre, identificacion):
       self.nombre = nombre
       self.identificacion = identificacion
   def get_nombre(self):
       return self.nombre