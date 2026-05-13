# ============================================================
# Clase Reserva del sistema
# Autor: KAROL YULIANA VARGAS RIZO
# ============================================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # ========================================================
    # Confirmar reserva
    # ========================================================
    def confirmar(self):
        self.estado = "Confirmada"
        print("Reserva confirmada exitosamente")

    # ========================================================
    # Cancelar reserva
    # ========================================================
    def cancelar(self):
        self.estado = "Cancelada"
        print("Reserva cancelada")

    # ========================================================
    # Mostrar información
    # ========================================================
    def mostrar_reserva(self):
        print("\n===== INFORMACIÓN DE LA RESERVA =====")
        print("Cliente:", self.cliente)
        print("Servicio:", self.servicio)
        print("Duración:", self.duracion)
        print("Estado:", self.estado)
        print("=====================================")


# ============================================================
# PRUEBA DEL SISTEMA
# ============================================================

# Crear reserva
reserva1 = Reserva("Carlos", "Corte de cabello", "1 hora")

# Mostrar datos iniciales
reserva1.mostrar_reserva()

# Confirmar reserva
reserva1.confirmar()

# Mostrar nuevamente
reserva1.mostrar_reserva()

# Cancelar reserva
reserva1.cancelar()

# Mostrar estado final
reserva1.mostrar_reserva()