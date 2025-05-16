class maquina:
    def __init__(self, nombre, piezas_requeridas, cantidad_piezas):
        self.nombre = nombre
        self.piezas_requeridas = piezas_requeridas
        def mostrar_requerimientos(self):
            print(f"Requerimientos para {self.descripcion}:")
            for i in range(len(self.piezas_requeridas)):
                pieza = self.piezas_requeridas[i]
                cantidad = self.cantidad_piezas[i]  # Cantidad requerida para ESTA máquina
                costo_parcial = pieza.costo * cantidad
                total_costo += costo_parcial
                print(f"- {pieza.desc}: {pieza.cantidad} unidades (Costo unitario: ${pieza.costo})")
            print(f"  Costo total: ${total_costo}")