from base_de_datos import guardar, eliminar_todos, obtener_todos, actualizar_estado

class Pedido:
    def __init__(self, numPedido, tienda, productos):
        self.numPedido = numPedido
        self.tienda = tienda
        self.productos = productos
        self.estado = "Pendiente"


class NodoArbol:
    def __init__(self, pedido):
        self.pedido = pedido
        self.izquierda = None
        self.derecha = None


class ArbolPedidos:
    def __init__(self):
        self.raiz = None
        self.contador = 1
        self.cargar_pedidos()

    def vacia(self):
        return self.raiz is None

    def contar_pedidos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)

    def cargar_pedidos(self):
        pedidos = obtener_todos()
        for numero, tienda, productos, estado in pedidos:
            if numero >= self.contador:
                self.contador = numero + 1
            self.agregar_pedido(tienda, productos)
            pedido = self.buscar_pedido(numero)
            if pedido:
                pedido.estado = estado
        if pedidos:
            print(f"Cargados {len(pedidos)} pedidos")

    def agregar_pedido(self, tienda, productos):
        numPedido = self.contador
        self.contador += 1
        nuevo = Pedido(numPedido, tienda, productos)
        self.raiz = self._insertar(self.raiz, nuevo)
        guardar(numPedido, tienda, productos, "Pendiente")
        print("Pedido creado con exito")
        print(f"Numero de pedido: {numPedido}")

    def _insertar(self, nodo, pedido):
        if nodo is None:
            return NodoArbol(pedido)
        if pedido.numPedido < nodo.pedido.numPedido:
            nodo.izquierda = self._insertar(nodo.izquierda, pedido)
        else:
            nodo.derecha = self._insertar(nodo.derecha, pedido)
        return nodo

    def buscar_pedido(self, numPedido):
        pedido = self._buscar(self.raiz, numPedido)
        if pedido:
            print(f"Pedido {pedido.numPedido} - {pedido.tienda} - {pedido.productos} - {pedido.estado}")
            return pedido
        else:
            print("Ese pedido no aparece.")
            return None

    def _buscar(self, nodo, numPedido):
        if nodo is None:
            return None
        if nodo.pedido.numPedido == numPedido:
            return nodo.pedido
        if numPedido < nodo.pedido.numPedido:
            return self._buscar(nodo.izquierda, numPedido)
        return self._buscar(nodo.derecha, numPedido)

    def imprimir_ordenado(self):
        if self.raiz is None:
            print("No hay nada guardado.")
            return
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            p = nodo.pedido
            print(f"{p.numPedido} | {p.tienda} | {p.productos} | {p.estado}")
            self._inorden(nodo.derecha)

    def enviar_pedido(self, numPedido):
        pedido = self._buscar(self.raiz, numPedido)
        if pedido:
            pedido.estado = "Enviado"
            actualizar_estado(pedido.numPedido, pedido.estado)
            print(f"Pedido {numPedido} ya va en camino.")
        else:
            print("No se encontró ese pedido.")

    def marcar_entregado(self, numPedido):
        pedido = self._buscar(self.raiz, numPedido)
        if pedido:
            pedido.estado = "Entregado"
            actualizar_estado(pedido.numPedido, pedido.estado)
            print(f"Pedido {numPedido} ya se entregó.")
        else:
            print("No se encontró ese pedido.")

    def pedidos_pendientes(self):
        contador = self._contar_pendientes(self.raiz)
        print(f"Quedan {contador} pendientes.")
        return contador

    def _contar_pendientes(self, nodo):
        if nodo is None:
            return 0
        contador = 1 if nodo.pedido.estado == "Pendiente" else 0
        return contador + self._contar_pendientes(nodo.izquierda) + self._contar_pendientes(nodo.derecha)

    def mostrar_pedidos_por_tienda(self, tienda):
        encontrado = self._buscar_tienda(self.raiz, tienda)
        if not encontrado:
            print("No hay pedidos de esa tienda.")

    def _buscar_tienda(self, nodo, tienda):
        if nodo is None:
            return False
        encontrado = False
        if nodo.pedido.tienda == tienda:
            p = nodo.pedido
            print(f"{p.numPedido} | {p.productos} | {p.estado}")
            encontrado = True
        izq = self._buscar_tienda(nodo.izquierda, tienda)
        der = self._buscar_tienda(nodo.derecha, tienda)
        return encontrado or izq or der

    def altura(self):
        altura = self._altura(self.raiz)
        print(f"Altura: {altura}")
        return altura

    def _altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def pedidos_en_rango(self, num_min, num_max):
        print(f"Pedidos del {num_min} al {num_max}")
        encontrados = self._rango(self.raiz, num_min, num_max)
        if not encontrados:
            print("No hay pedidos en ese rango.")

    def _rango(self, nodo, num_min, num_max):
        if nodo is None:
            return False
        encontrado = False
        if nodo.pedido.numPedido > num_min:
            encontrado = self._rango(nodo.izquierda, num_min, num_max) or encontrado
        if num_min <= nodo.pedido.numPedido <= num_max:
            p = nodo.pedido
            print(f"{p.numPedido} | {p.tienda} | {p.productos} | {p.estado}")
            encontrado = True
        if nodo.pedido.numPedido < num_max:
            encontrado = self._rango(nodo.derecha, num_min, num_max) or encontrado
        return encontrado

    def limpiar(self):
        self.raiz = None
        self.contador = 1
        eliminar_todos()
        print("Se elimino todo.")