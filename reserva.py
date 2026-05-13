# ============================================================
# SISTEMA INTEGRAL DE GESTIÓN DE CLIENTES, SERVICIOS Y RESERVAS
# Clase Reserva del sistema
# Autor: KAROL YULIANA VARGAS RIZO
# ============================================================

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"
        print("Reserva confirmada")

    def mostrar_reserva(self):
        print("Cliente:", self.cliente)
        print("Servicio:", self.servicio)
        print("Duración:", self.duracion)
        print("Estado:", self.estado)


# ==========================
# PRUEBA DEL SISTEMA
# ==========================

reserva1 = Reserva("Carlos", "Corte de cabello", "1 hora")

reserva1.mostrar_reserva()

reserva1.confirmar()

reserva1.mostrar_reserva()