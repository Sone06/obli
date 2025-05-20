from pieza import Pieza

class Reposicion:
    def __init__(self, pieza, cantidad_lotes, fecha):
        self.pieza = pieza
        self.cantidad_lotes = cantidad_lotes
        self.fecha = fecha

    def costo(self):
        return self.cantidad_lotes * Pieza.costo_unitario

    def __str__(self):
        return f"Reposición: Pieza {self.pieza.descripcion}, Lotes: {self.cantidad_lotes}, Fecha: {self.fecha}, Costo: ${self.costo():.2f}"
