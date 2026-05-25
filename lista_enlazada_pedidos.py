from base_de_datos import guardar, eliminar, eliminar_todos, obtener_todos, actualizar_estado
class Pedido:
    def __init__(self, numPedido, tienda, productos, fechaEntrega):
        self.numPedido = numPedido
        self.tienda = tienda
        self.productos = productos
        self.fechaEntrega = fechaEntrega
        self.estado = "Pendiente"
        self.siguiente = None


class ListaPedidos:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0
        self.cargar_pedidos()

    def cargar_pedidos(self):
        pedidos = obtener_todos()
        for numero, tienda, productos, estado in pedidos:
            self.agregar_pedido(numero, tienda, productos, "Sin fecha")
            pedido = self.buscar_pedido(numero)
            if pedido:
                pedido.estado = estado
        if pedidos:
            print(f"Cargados {len(pedidos)} pedidos")
    
    def vacia(self):
        if self.cabeza is None:
            return True
        return False
        
    def contar_pedidos(self):
        return self.tamano
    

    def agregar_pedido(self, numPedido, tienda, productos, fechaEntrega):
        nuevo = Pedido(numPedido, tienda, productos, fechaEntrega)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1
        guardar(numPedido, tienda, productos, "Pendiente")


    def imprimir_pedidos(self):
        if self.vacia():
            print("No hay pedidos para imprimir.")
            return
        else:
            actual = self.cabeza
            while actual is not None:
                print(f"Pedido #{actual.numPedido} - Tienda: {actual.tienda} - Productos: {actual.productos} - Fecha de Entrega: {actual.fechaEntrega} - Estado: {actual.estado}")
                actual = actual.siguiente
            print("Los Pedidos han sido impresos.")
    

    def enviar_pedido(self, numPedido):
        actual = self.cabeza
        while actual is not None:
            if actual.numPedido == numPedido:
                actual.estado = "Enviado"
                actualizar_estado(actual.numPedido, actual.estado)
                print(f"Pedido #{numPedido} ha sido enviado a la tienda {actual.tienda}.")
                return
            actual = actual.siguiente
        print(f"Pedido #{numPedido} no encontrado.")
    

    def buscar_pedido(self, numPedido):
        actual = self.cabeza
        while actual is not None:
            if actual.numPedido == numPedido:
                return actual
            actual = actual.siguiente
        return None


    def agregar_pedido_final(self, numPedido, tienda, productos, fechaEntrega):
        nuevo = Pedido(numPedido, tienda, productos, fechaEntrega)
        if self.vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano += 1
        guardar(numPedido, tienda, productos, "Pendiente")
        print(f"Pedido #{numPedido} agregado al final.")


    def eliminar_pedido(self, numPedido):
        if self.vacia():
            print("No hay pedidos para eliminar.")
            return
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.numPedido == numPedido:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamano -= 1
                eliminar(numPedido)
                print(f"Pedido #{numPedido} eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
        print("Pedido no encontrado.")


    def actualizar_fecha_entrega(self, numPedido, nuevaFecha):
        actual = self.cabeza
        while actual is not None:
            if actual.numPedido == numPedido:
                actual.fechaEntrega = nuevaFecha
                print(f"Fecha de entrega del pedido #{numPedido} actualizada a {nuevaFecha}")
                return
            actual = actual.siguiente
        print("Pedido no encontrado.")


    def marcar_entregado(self, numPedido):
        actual = self.cabeza
        while actual is not None:
            if actual.numPedido == numPedido:
                actual.estado = "Entregado"
                actualizar_estado(actual.numPedido, actual.estado)
                print(f"Pedido #{numPedido} fue entregado.")
                return
            actual = actual.siguiente
        print("Pedido no encontrado.")


    def pedidos_pendientes(self):
        actual = self.cabeza
        contador = 0
        while actual is not None:
            if actual.estado == "Pendiente":
                contador += 1
            actual = actual.siguiente
        print(f"Pedidos pendientes: {contador}")
        return contador


    def mostrar_pedidos_por_tienda(self, tienda):
        actual = self.cabeza
        encontrado = False
        while actual is not None:
            if actual.tienda == tienda:
                print(f"Pedido #{actual.numPedido} - Productos: {actual.productos} - Fecha: {actual.fechaEntrega} - Estado: {actual.estado}")
                encontrado = True
            actual = actual.siguiente
        if not encontrado:
            print("No hay pedidos para esta tienda.")


    def limpiar_lista(self):
        self.cabeza = None
        self.tamano = 0
        eliminar_todos()
        print("Todos los pedidos han sido eliminados.")