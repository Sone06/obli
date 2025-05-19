class pedido:
    todos_los_pedidos = []
    def __init__(self, cliente, maquina, fechaRecibido, fechaEntregado,estado):
        self.cliente = cliente
        self.maquina = maquina
        self.fechaRecibido = fechaRecibido
        self.fechaEntregado = fechaEntregado
        self.estado =   "Pendiente"
        self.todos_los_pedidos.append(self)
    def agregar_maquina(self, nueva_maquina):
        """Agrega una máquina adicional al pedido"""
        if isinstance(self.maquina_requerida, list):
            self.maquina_requerida.append(nueva_maquina)
        else:
            # Si inicialmente era solo una máquina, convertimos a lista
            self.maquina_requerida = [self.maquina_requerida, nueva_maquina]
    def confirmar_pedido(self):
        self.estado = "Confirmado"
        for maquina in self.maquina_requerida:
            i+=1
            if maquina.piezas_requeridas[i] > maquina.piezas.cantidad:
                print(f"Faltan {maquina.piezas} para la máquina {maquina.nombre}. No se puede confirmar el pedido.")
                return
            else: maquina.piezas.cantidad-= maquina.cantidad_piezas[i]
  


    def mostrar_pedidos_pendientes(self,cls):
        print("\n=== PEDIDOS PENDIENTES (TODAS LAS INSTANCIAS) ===")
        for pedido in cls.todos_los_pedidos:
            if pedido.estado == "Pendiente":
                print(f"Cliente: {pedido.cliente}")
                print(f"Máquina: {pedido.maquina_requerida.nombre}\n")


    def agregar_requerimiento(self):
        pass
    def disponibilidad(self):
        pass
    def costo_produccion(self):
        pass


    
