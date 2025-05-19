
class Pieza:
    def __init__(self,descPieza,costoPieza,cantidadPieza):
        self.codigo=0
        self.descPieza=descPieza
        self.costoPieza=costoPieza
        self.cantidadPieza=cantidadPieza

        def __str__(self):
            return f"{self.codigo} {self.descPieza} {self.costoPieza} {self.cantidadPieza}"
