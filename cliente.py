class cliente:
    def __init__(self, id, contacto, tipo_cliente):
        self.id = id
        self.contacto = contacto
        self.tipo_cliente = tipo_cliente




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






class pedido:
    todos_los_pedidos = []
    def __innit__(self, cliente, maquina_requerida):
        self.cliente = cliente
        self.maquina_requerida = maquina_requerida
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
  


    def mostrar_pedidos_pendientes(cls):
        print("\n=== PEDIDOS PENDIENTES (TODAS LAS INSTANCIAS) ===")
        for pedido in cls.todos_los_pedidos:
            if pedido.estado == "Pendiente":
                print(f"Cliente: {pedido.cliente}")
                print(f"Máquina: {pedido.maquina_requerida.nombre}\n")
    def actualiza_pedidos():
        for pedido in cls.todos_los_pedidos:
            if pedido






class Pieza:
    def __init__(self,desc,costo,tamano,cantidad):
        self.desc=desc
        self.costo=costo
        self.tamano=tamano
        self.cantidad=cantidad 