# ============================================
# CLASE LOGGER
# ============================================
class Logger:
    def log(self, mensaje):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}\n")

        print(f"LOG: {mensaje}")