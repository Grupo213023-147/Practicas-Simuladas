# ============================================================
# SClases Servicio
# Autor: KAROL YULIANA VARGAS RIZO
#
# Funciones principales:
# - Registro de servicios
# - Clasificación de servicios por categoría
# - Gestión de precios
# - Visualización de detalles del servicio
# ============================================================ 
class Servicio:
    def _init_(self, nombre, precio):
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
