import tkinter as tk
from tkinter import messagebox

from cliente import Cliente
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
from logger import Logger

clientes = []
servicios = []
reservas = []
logger = Logger()

# -------------------------
# FUNCIONES
# -------------------------

def crear_cliente():
    try:
        nombre = entry_nombre.get()
        identificacion = entry_id.get()

        cliente = Cliente(nombre, identificacion)
        clientes.append(cliente)

        messagebox.showinfo("Éxito", "Cliente creado")
        entry_nombre.delete(0, tk.END)
        entry_id.delete(0, tk.END)

    except Exception as e:
        logger.log(str(e))
        messagebox.showerror("Error", str(e))


def crear_servicio():
    try:
        nombre = entry_servicio.get()
        precio = float(entry_precio.get())
        tipo = tipo_servicio.get()

        if tipo == "Sala":
            servicio = ServicioSala(nombre, precio)
        elif tipo == "Equipo":
            servicio = ServicioEquipo(nombre, precio)
        elif tipo == "Asesoria":
            servicio = ServicioAsesoria(nombre, precio)
        else:
            raise ValueError("Seleccione un tipo válido")

        servicios.append(servicio)
        messagebox.showinfo("Éxito", "Servicio creado")

    except Exception as e:
        logger.log(str(e))
        messagebox.showerror("Error", str(e))


def crear_reserva():
    try:
        idx_cliente = lista_clientes.curselection()[0]
        idx_servicio = lista_servicios.curselection()[0]
        duracion = int(entry_duracion.get())

        reserva = Reserva(clientes[idx_cliente], servicios[idx_servicio], duracion)
        reservas.append(reserva)

        messagebox.showinfo("Éxito", "Reserva creada")
        actualizar_listas()

    except Exception as e:
        logger.log(str(e))
        messagebox.showerror("Error", str(e))


def confirmar_reserva():
    try:
        idx = lista_reservas.curselection()[0]
        reservas[idx].confirmar()
        actualizar_listas()

    except Exception as e:
        logger.log(str(e))
        messagebox.showerror("Error", str(e))


def actualizar_listas():
    lista_clientes.delete(0, tk.END)
    for c in clientes:
        lista_clientes.insert(tk.END, c.get_nombre())

    lista_servicios.delete(0, tk.END)
    for s in servicios:
        lista_servicios.insert(tk.END, s.descripcion())

    lista_reservas.delete(0, tk.END)
    for r in reservas:
        texto = f"{r.cliente.get_nombre()} - {r.servicio.descripcion()} - {r.estado}"
        lista_reservas.insert(tk.END, texto)


# -------------------------
# INTERFAZ
# -------------------------

ventana = tk.Tk()
ventana.title("Sistema de Reservas FJ")
ventana.geometry("600x500")

# CLIENTES
tk.Label(ventana, text="Cliente").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Button(ventana, text="Crear Cliente", command=crear_cliente).pack()

# SERVICIOS
tk.Label(ventana, text="Servicio").pack()
entry_servicio = tk.Entry(ventana)
entry_servicio.pack()

entry_precio = tk.Entry(ventana)
entry_precio.pack()

tipo_servicio = tk.StringVar(value="Sala")
tk.OptionMenu(ventana, tipo_servicio, "Sala", "Equipo", "Asesoria").pack()

tk.Button(ventana, text="Crear Servicio", command=crear_servicio).pack()

# RESERVAS
tk.Label(ventana, text="Duración").pack()
entry_duracion = tk.Entry(ventana)
entry_duracion.pack()

tk.Label(ventana, text="Clientes").pack()
lista_clientes = tk.Listbox(ventana)
lista_clientes.pack()

tk.Label(ventana, text="Servicios").pack()
lista_servicios = tk.Listbox(ventana)
lista_servicios.pack()

tk.Button(ventana, text="Crear Reserva", command=crear_reserva).pack()

# LISTA RESERVAS
tk.Label(ventana, text="Reservas").pack()
lista_reservas = tk.Listbox(ventana)
lista_reservas.pack()

tk.Button(ventana, text="Confirmar Reserva", command=confirmar_reserva).pack()

# INICIAR
ventana.mainloop()