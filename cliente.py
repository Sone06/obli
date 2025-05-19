from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, id, telefono, correoE):
        self.id = id
        self.telefono = telefono
        self.correoE = correoE

    @abstractmethod
    def mostrar_datos(self):
        pass


class ClienteParticular(Cliente):
    def __init__(self, id, telefono, correoE, cedula, nombreCompleto):
        super().__init__(id, telefono, correoE)
        self.cedula = cedula
        self.nombreCompleto = nombreCompleto

    def mostrar_datos(self):
        print(f"Cliente Particular:")
        print(f"Nombre: {self.nombreCompleto}")
        print(f"Cédula: {self.cedula}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correoE}")


class Empresa(Cliente):
    def __init__(self, id, telefono, correoE, RUT, nombre, paginaWeb):
        super().__init__(id, telefono, correoE)
        self.RUT = RUT
        self.nombre = nombre
        self.paginaWeb = paginaWeb

    def mostrar_datos(self):
        print(f"Empresa:")
        print(f"Nombre: {self.nombre}")
        print(f"RUT: {self.RUT}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correoE}")
        print(f"Web: {self.paginaWeb}")











