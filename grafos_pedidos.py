from collections import defaultdict, deque
from base_de_datos import guardar, eliminar_todos, obtener_todos, actualizar_estado

class Pedido:
    def __init__(self, numPedido, tienda, productos):
        self.numPedido = numPedido
        self.tienda = tienda
        self.productos = productos
        self.estado = "Pendiente"
        self.siguiente = None


class NodoArbol:
    def __init__(self, pedido):
        self.pedido = pedido
        self.izquierda = None
        self.derecha = None


class GrafoTiendas:
    def __init__(self):
        self.grafo = defaultdict(list)
        self.tiendas = set()
    
    def agregar_tienda(self, tienda):
        if tienda not in self.tiendas:
            self.tiendas.add(tienda)
            self.grafo[tienda] = []
            print(f"Tienda '{tienda}' agregada.")
    
    def agregar_ruta(self, tienda_origen, tienda_destino, distancia=1):
        if tienda_origen not in self.tiendas:
            self.agregar_tienda(tienda_origen)
        if tienda_destino not in self.tiendas:
            self.agregar_tienda(tienda_destino)
        
        for i, (dest, dist) in enumerate(self.grafo[tienda_origen]):
            if dest == tienda_destino:
                self.grafo[tienda_origen][i] = (tienda_destino, distancia)
                print(f"Ruta actualizada: {tienda_origen} -> {tienda_destino} ({distancia} km)")
                return
        
        self.grafo[tienda_origen].append((tienda_destino, distancia))
        print(f"Ruta agregada: {tienda_origen} -> {tienda_destino} ({distancia} km)")
    
    def mostrar_grafo(self):
        if not self.tiendas:
            print("El grafo está vacío.")
            return
        
        print("\n=== GRAFO DE TIENDAS ===")
        for tienda in sorted(self.tiendas):
            if self.grafo[tienda]:
                rutas = ", ".join([f"{dest}({dist}km)" for dest, dist in self.grafo[tienda]])
                print(f"{tienda} -> {rutas}")
            else:
                print(f"{tienda} -> (sin conexiones)")
    
    def camino_mas_corto(self, origen, destino):
        if origen not in self.tiendas or destino not in self.tiendas:
            print("Tienda no encontrada.")
            return None
        
        distancias = {tienda: float('inf') for tienda in self.tiendas}
        distancias[origen] = 0
        visitadas = set()
        camino = {tienda: [] for tienda in self.tiendas}
        
        while len(visitadas) < len(self.tiendas):
            nodo_actual = None
            min_dist = float('inf')
            
            for tienda in self.tiendas:
                if tienda not in visitadas and distancias[tienda] < min_dist:
                    nodo_actual = tienda
                    min_dist = distancias[tienda]
            
            if nodo_actual is None or min_dist == float('inf'):
                break
            
            visitadas.add(nodo_actual)
            
            for vecino, distancia in self.grafo[nodo_actual]:
                nueva_dist = distancias[nodo_actual] + distancia
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    camino[vecino] = camino[nodo_actual] + [nodo_actual]
        
        if distancias[destino] == float('inf'):
            print(f"No hay ruta de {origen} a {destino}")
            return None
        
        ruta_completa = camino[destino] + [destino]
        print(f"\nCamino más corto de {origen} a {destino}:")
        print(f"  Ruta: {' -> '.join(ruta_completa)}")
        print(f"  Distancia total: {distancias[destino]} km")
        return ruta_completa, distancias[destino]
    
    def tiendas_conectadas(self, tienda):
        if tienda not in self.tiendas:
            print("Tienda no encontrada.")
            return
        
        visitadas = set()
        cola = deque([tienda])
        visitadas.add(tienda)
        
        print(f"\nTiendas alcanzables desde {tienda}:")
        while cola:
            actual = cola.popleft()
            if actual != tienda:
                print(f"  - {actual}")
            
            for vecino, _ in self.grafo[actual]:
                if vecino not in visitadas:
                    visitadas.add(vecino)
                    cola.append(vecino)
        
        if len(visitadas) == 1:
            print("  (Ninguna tienda conectada)")
    
    def componentes_conexos(self):
        visitadas = set()
        componentes = []
        
        for tienda in self.tiendas:
            if tienda not in visitadas:
                componente = set()
                cola = deque([tienda])
                visitadas.add(tienda)
                
                while cola:
                    actual = cola.popleft()
                    componente.add(actual)
                    
                    for vecino, _ in self.grafo[actual]:
                        if vecino not in visitadas:
                            visitadas.add(vecino)
                            cola.append(vecino)
                
                componentes.append(componente)
        
        print(f"\nComponentes conexas: {len(componentes)}")
        for i, comp in enumerate(componentes, 1):
            print(f"  Componente {i}: {', '.join(sorted(comp))}")

    def eliminar_tienda(self, tienda):
        if tienda not in self.tiendas:
            print(f"La tienda '{tienda}' no existe.")
            return
        self.tiendas.remove(tienda)
        del self.grafo[tienda]
        for origen in self.tiendas:
            self.grafo[origen] = [(d, dist) for d, dist in self.grafo[origen] if d != tienda]
        print(f"Tienda '{tienda}' eliminada.")

    def eliminar_ruta(self, origen, destino):
        if origen not in self.tiendas:
            print(f"La tienda '{origen}' no existe.")
            return
        self.grafo[origen] = [(d, dist) for d, dist in self.grafo[origen] if d != destino]
        print(f"Ruta {origen} -> {destino} eliminada.")

    def buscar_tienda(self, tienda):
        if tienda not in self.tiendas:
            print(f"La tienda '{tienda}' no existe.")
            return
        print(f"\nTienda: {tienda}")
        if self.grafo[tienda]:
            for dest, dist in self.grafo[tienda]:
                print(f"-> {dest} ({dist} km)")
        else:
            print("Sin rutas")

class ListaPedidos:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0
        self.raiz = None
        self.contador = 1
        self.grafo_tiendas = GrafoTiendas()
        self.cargar_pedidos()

    def cargar_pedidos(self):
        pedidos = obtener_todos()
        for numero, tienda, productos, estado in pedidos:
            if numero >= self.contador:
                self.contador = numero + 1
            self.agregar_pedido(tienda, productos)
            pedido = self._buscar_arbol(self.raiz, numero)
            if pedido:
                pedido.estado = estado
        if pedidos:
            print(f"Cargados {len(pedidos)} pedidos")

    def vacia(self):
        return self.cabeza is None

    def contar_pedidos(self):
        return self.tamano

    def agregar_pedido(self, tienda, productos):
        numPedido = self.contador
        self.contador += 1

        nuevo = Pedido(numPedido, tienda, productos)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1
        self.raiz = self._insertar_arbol(self.raiz, nuevo)
        
        if tienda not in self.grafo_tiendas.tiendas:
            self.grafo_tiendas.agregar_tienda(tienda)

        guardar(numPedido, tienda, productos, "Pendiente")

        print("Pedido creado con exito")
        print(f"Numero de pedido: {numPedido}")

    def _insertar_arbol(self, nodo, pedido):
        if nodo is None:
            return NodoArbol(pedido)

        if pedido.numPedido < nodo.pedido.numPedido:
            nodo.izquierda = self._insertar_arbol(nodo.izquierda, pedido)
        else:
            nodo.derecha = self._insertar_arbol(nodo.derecha, pedido)

        return nodo

    def buscar_pedido(self, numPedido):
        pedido = self._buscar_arbol(self.raiz, numPedido)

        if pedido:
            print(f"Pedido {pedido.numPedido} - {pedido.tienda} - {pedido.productos} - {pedido.estado}")
        else:
            print("Ese pedido no aparece.")

    def _buscar_arbol(self, nodo, numPedido):
        if nodo is None:
            return None

        if nodo.pedido.numPedido == numPedido:
            return nodo.pedido

        if numPedido < nodo.pedido.numPedido:
            return self._buscar_arbol(nodo.izquierda, numPedido)
        else:
            return self._buscar_arbol(nodo.derecha, numPedido)

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
        pedido = self._buscar_arbol(self.raiz, numPedido)

        if pedido:
            pedido.estado = "Enviado"
            actualizar_estado(pedido.numPedido, pedido.estado)
            print(f"Pedido {numPedido} ya va en camino.")
        else:
            print("No se encontró ese pedido.")

    def marcar_entregado(self, numPedido):
        pedido = self._buscar_arbol(self.raiz, numPedido)

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

    def altura_arbol(self):
        altura = self._altura(self.raiz)
        print(f"Altura: {altura}")
        return altura

    def _altura(self, nodo):
        if nodo is None:
            return 0

        return 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def limpiar_lista(self):
        self.cabeza = None
        self.raiz = None
        self.tamano = 0
        self.contador = 1
        eliminar_todos()
        print("Se borró todo.")

    def pedidos_en_rango(self, num_min, num_max):
        print(f"Pedidos del {num_min} al {num_max}")
        encontrados = self._rango_arbol(self.raiz, num_min, num_max)
        if not encontrados:
            print("No hay pedidos en ese rango.")
            
    def eliminar_tienda_del_grafo(self, tienda):
        self.grafo_tiendas.eliminar_tienda(tienda)
        
    def _rango_arbol(self, nodo, num_min, num_max):
        if nodo is None:
            return False
        encontrado = False
        if nodo.pedido.numPedido > num_min:
            encontrado = self._rango_arbol(nodo.izquierda, num_min, num_max) or encontrado
        if num_min <= nodo.pedido.numPedido <= num_max:
            p = nodo.pedido
            print(f"{p.numPedido} | {p.tienda} | {p.productos} | {p.estado}")
            encontrado = True
        if nodo.pedido.numPedido < num_max:
            encontrado = self._rango_arbol(nodo.derecha, num_min, num_max) or encontrado
        return encontrado
