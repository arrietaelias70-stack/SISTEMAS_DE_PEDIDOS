from lista_enlazada_pedidos import ListaPedidos as ListaV1
from arbol_binario_pedidos import ArbolPedidos as ListaV2
from grafos_pedidos import ListaPedidos as ListaFinal
from grafos_pedidos import GrafoTiendas
import os
class SistemaGestion:
    def __init__(self):
        self.modo = "final"
        self.sistema_final = ListaFinal()
        self.sistema_v2 = ListaV2()
        self.sistema_v1 = ListaV1()
        self.grafo_standalone = GrafoTiendas()
    
    def obtener_sistema(self):
        if self.modo == "v1":
            return self.sistema_v1, "Lista enlazada"
        elif self.modo == "v2":
            return self.sistema_v2, "arbol binario"
        else:
            return self.sistema_final, "Grafo + arbol + lista enlazada"
    
    def cambiar_modo(self, modo):
        if modo in ["v1", "v2", "final"]:
            self.modo = modo
            return True
        return False


sistema = SistemaGestion()

print("Sistema de gestion de pedidos")

while True:
    sistema_actual, nombre_modo = sistema.obtener_sistema()
    
    print(f"Modo actual: {nombre_modo}")
    print("\nGESTION DE PEDIDOS")
    print("1. Agregar pedido")
    print("2. Buscar pedido")
    print("3. Enviar pedido")
    print("4. Marcar entregado")
    print("5. Mostrar pedidos")
    print("6. Pedidos pendientes")
    print("7. Mostrar pedidos por tienda")
    print("8. Altura del arbol")
    print("9. Pedidos en rango")
    print("10. Agregar pedido al final modo V1")
    print("11. Eliminar pedido modo V1")
    print("12. Actualizar fecha entrega modo V1)")
    print("13. Limpiar lista")
    print("\n GRAFO DE TIENDAS")
    print("14. Agregar tienda al grafo")
    print("15. Agregar ruta entre tiendas")
    print("16. Mostrar grafo")
    print("17. Camino mas corto")
    print("18. Tiendas alcanzables")
    print("19. Componentes conexas")
    print("\nCONFIGURACION DEL SISTEMA")
    print("20. Cambiar modo V1, V2 o el Final)")
    print("21. Abrir la web")
    print("0. Salir")
    
    opcion = input("Escoge una opcion por favor: ")
    
    if opcion == "1":
        if sistema.modo == "v1":
            num = int(input("Numero de pedido: "))
            tienda = input("Tienda: ")
            productos = input("Productos: ")
            fecha = input("Fecha de entrega: ")
            sistema_actual.agregar_pedido(num, tienda, productos, fecha)
        else:
            tienda = input("Tienda: ")
            productos = input("Productos: ")
            sistema_actual.agregar_pedido(tienda, productos)
    
    elif opcion == "2":
        num =int(input("Numero de pedido: "))
        sistema_actual.buscar_pedido(num)
    
    elif opcion == "3":
        num = int(input("Numero de pedido: "))
        sistema_actual.enviar_pedido(num)
    
    elif opcion == "4":
        num = int(input("Numero de pedido: "))
        sistema_actual.marcar_entregado(num)
    
    elif opcion == "5":
        if sistema.modo == "v1":
            sistema_actual.imprimir_pedidos()
        else:
            sistema_actual.imprimir_ordenado()
    
    elif opcion == "6":
        sistema_actual.pedidos_pendientes()
    
    elif opcion == "7":
        tienda = input("Tienda: ")
        sistema_actual.mostrar_pedidos_por_tienda(tienda)
    
    elif opcion == "8":
        if sistema.modo == "v1":
            print("La lista enlazada no tiene altura, cambiate al modo v2 o final.")
        else:
            sistema_actual.altura_arbol()
    
    elif opcion == "9":
        if sistema.modo == "v1":
            print("La lista enlazada no tiene busqueda por rango, cambiate al modo v2 o final")
        else:
            min_num = int(input("Desde numero: "))
            max_num = int(input("Hasta numero: "))
            sistema_actual.pedidos_en_rango(min_num, max_num)
    
    elif opcion == "10":
        if sistema.modo == "v1":
            num = int(input("Numero de pedido: "))
            tienda = input("Tienda: ")
            productos = input("Productos: ")
            fecha = input("Fecha de entrega: ")
            sistema_actual.agregar_pedido_final(num, tienda, productos, fecha)
        else:
            print("Esta opcion solo disponible en el modo v1.")
    
    elif opcion == "11":
        if sistema.modo == "v1":
            num = int(input("Numero de pedido: "))
            sistema_actual.eliminar_pedido(num)
        else:
            print("Esta opcion solo disponible en el modo v1.")
    
    elif opcion == "12":
        if sistema.modo == "v1":
            num = int(input("Numero de pedido: "))
            nueva_fecha = input("Nueva fecha de entrega: ")
            sistema_actual.actualizar_fecha_entrega(num, nueva_fecha)
        else:
            print("Esta opcion solo disponible en el modo v1.")
    
    elif opcion == "13":
        sistema_actual.limpiar_lista()
    
    elif opcion == "14":
        tienda = input("Nombre de la tienda: ")
        if sistema.modo == "final":
            sistema_actual.grafo_tiendas.agregar_tienda(tienda)
        else:
            sistema.grafo_standalone.agregar_tienda(tienda)
    
    elif opcion == "15":
        origen = input("Tienda origen: ")
        destino = input("Tienda destino: ")
        distancia = int(input("Distancia en km: "))
        if sistema.modo == "final":
            sistema_actual.grafo_tiendas.agregar_ruta(origen, destino, distancia)
        else:
            sistema.grafo_standalone.agregar_ruta(origen, destino, distancia)
    
    elif opcion == "16":
        if sistema.modo == "final":
            sistema_actual.grafo_tiendas.mostrar_grafo()
        else:
            sistema.grafo_standalone.mostrar_grafo()
    
    elif opcion == "17":
        origen = input("Tienda origen: ")
        destino = input("Tienda destino: ")
        if sistema.modo == "final":
            sistema_actual.grafo_tiendas.camino_mas_corto(origen, destino)
        else:
            sistema.grafo_standalone.camino_mas_corto(origen, destino)
    
    elif opcion == "18":
        tienda = input("Tienda: ")
        if sistema.modo == "final":
            sistema_actual.grafo_tiendas.tiendas_conectadas(tienda)
        else:
            sistema.grafo_standalone.tiendas_conectadas(tienda)
    
    elif opcion == "19":
        if sistema.modo == "final":
            sistema_actual.grafo_tiendas.componentes_conexos()
        else:
            sistema.grafo_standalone.componentes_conexos()
    
    elif opcion == "20":
        print("\nModos disponibles:")
        print("1. Lista enlazada V1")
        print("2. Arbol binario V2")
        print("3. Grafo + Arbol + Lista modo final)")
        modo_opcion = input("Elige modo: ")
        if modo_opcion == "1":
            sistema.cambiar_modo("v1")
            print("Cambiado a lista enlazada V1")
        elif modo_opcion == "2":
            sistema.cambiar_modo("v2")
            print("Cambiado a arbol binario V2")
        elif modo_opcion == "3":
            sistema.cambiar_modo("final")
            print("Cambiado a GRAFO + ARBOL + LISTA")
        else:
            print("Opcion invalida")
    elif opcion == "21":
        os.system("streamlit run app.py")
    elif opcion == "0":
        print("Fin del programa.")
        break
    
    else:
        print("Opcion invalida")