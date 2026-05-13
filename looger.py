# ============================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES
# SERVICIOS Y RESERVAS
# Clase Logger del sistema
# ============================================

class Logger:

    def log(self, mensaje):

        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}\n")

        print(f"LOG: {mensaje}")


# ============================================
# PRUEBA DEL SISTEMA
# ============================================

logger = Logger()

logger.log("Sistema iniciado correctamente")
logger.log("Nueva reserva registrada")
logger.log("Servicio actualizado")