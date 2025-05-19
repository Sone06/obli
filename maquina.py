class maquina:
    def __init__(self, codigo, descripcion,):

        self.codigo = codigo
        self.descripcion = descripcion
        self.piezas_requeridas = []   # Lista de piezas (objeto Pieza)
        self.cantidades = []          # Lista de cantidades requeridas de cada pieza

    def agregar_requerimiento(self, pieza, cantidad):
        """Agrega una pieza y la cantidad necesaria para fabricar una unidad de esta máquina."""
        self.piezas_requeridas.append(pieza)
        self.cantidades.append(cantidad)

    def disponibilidad(self):
        """Verifica si hay suficientes piezas en stock para fabricar una unidad de esta máquina."""
        for i in range(len(self.piezas_requeridas)):
            pieza = self.piezas_requeridas[i]
            cantidad_necesaria = self.cantidades[i]
            if pieza.cantidad < cantidad_necesaria:
                print(f"No hay suficiente de la pieza '{pieza.nombre}': se necesita {cantidad_necesaria}, hay {pieza.cantidad}.")
                return False
        print(f"Todas las piezas están disponibles para fabricar una '{self.descripcion}'.")
        return True

    def costo_produccion(self):
        """Calcula el costo total de fabricar una unidad de esta máquina."""
        total = 0
        for i in range(len(self.piezas_requeridas)):
            pieza = self.piezas_requeridas[i]
            cantidad = self.cantidades[i]
            total += pieza.costo_unitario * cantidad
        return total
        pass    
