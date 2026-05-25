import streamlit as st
from lista_enlazada_pedidos import ListaPedidos as ListaV1
from arbol_binario_pedidos import ArbolPedidos as ListaV2
from grafos_pedidos import ListaPedidos as ListaFinal
from grafos_pedidos import GrafoTiendas


st.set_page_config(page_title="Sistema de Gestion de Pedidos", layout="wide")


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background-color: #0b0f19;
    }
    h1, h2, h3, h4 {
        color: #f8fafc !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em;
    }
    .stButton button {
        background-color: #1e293b !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 8px 16px;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }
    .stButton button:hover {
        background-color: #2563eb !important;
        border-color: #3b82f6 !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }
    /* Contenedores nativos estilizados */
    div[data-testid="stExpander"], div[data-testid="stContainer"], div[data-testid="stForm"] {
        background-color: #111827;
        border: 1px solid #1f2937 !important;
        border-radius: 12px;
        padding: 24px;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox div {
        background-color: #1f2937 !important;
        color: #f8fafc !important;
        border-radius: 8px !important;
        border: 1px solid #374151 !important;
    }
    button[data-baseweb="tab"] {
        color: #94a3b8 !important;
        font-size: 1rem;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #3b82f6 !important;
        border-bottom-color: #3b82f6 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Sistema de Gestión de Pedidos")
st.caption("Estructuras de Datos | Lista Enlazada | Arbol Binario | Grafo")


if 'estructuras' not in st.session_state:
    st.session_state.estructuras = {
        "Final (Grafo)": ListaFinal(),
        "Árbol Binario": ListaV2(),
        "Lista Enlazada": ListaV1()
    }
    st.session_state.grafo_aux = GrafoTiendas()


with st.sidebar:
    st.markdown("## Configuración")
    opcion = st.radio(
        "Seleccione estructura",
        list(st.session_state.estructuras.keys()),
        index=0
    )
    st.markdown("---")
    st.markdown(f"Modo activo: **{opcion}**")
    st.caption("Los cambios en los pedidos se sincronizan de forma automática.")


sistema = st.session_state.estructuras[opcion]
grafo_activo = sistema.grafo_tiendas if opcion == "Final (Grafo)" else st.session_state.grafo_aux

tab1, tab2, tab3 = st.tabs(["Pedidos", "Grafo de Tiendas", "Estadísticas"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Nuevo Pedido")
        tienda = st.text_input("Tienda", placeholder="Ej: Tienda Central")
        productos = st.text_input("Productos", placeholder="Ej: Componentes")
        
        if opcion == "Lista Enlazada":
            numero = st.number_input("Número de pedido", min_value=1, step=1)
            fecha = st.text_input("Fecha de entrega", placeholder="AAAA-MM-DD")
            if st.button("Agregar pedido", use_container_width=True, key="btn_add_v1"):
                sistema.agregar_pedido(numero, tienda, productos, fecha)
                st.success("Pedido registrado exitosamente")
        else:
            if st.button("Agregar pedido", use_container_width=True, key="btn_add_tree_graph"):
                sistema.agregar_pedido(tienda, productos)
                st.success("Pedido registrado exitosamente")
                
    with col2:
        st.markdown("### Buscar Pedido")
        num_buscar = st.number_input("Número de pedido", min_value=1, step=1, key="buscar")
        if st.button("Buscar", use_container_width=True):
            sistema.buscar_pedido(num_buscar)
            
    st.markdown("### Acciones Rápidas")
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        if st.button("Enviar", use_container_width=True):
            sistema.enviar_pedido(num_buscar)
    with col_b:
        if st.button("Entregar", use_container_width=True):
            sistema.marcar_entregado(num_buscar)
    with col_c:
        if st.button("Ver todos", use_container_width=True):
            sistema.imprimir_pedidos() if opcion == "Lista Enlazada" else sistema.imprimir_ordenado()
    with col_d:
        if st.button("Limpiar todo", use_container_width=True):
            sistema.limpiar_lista()
            st.toast("Todos los registros fueron eliminados")

with tab2:
    st.markdown("### Gestión de Tiendas y Rutas")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Agregar Tienda")
        nueva_tienda = st.text_input("Nombre de la tienda", key="nueva_tienda")
        if st.button("Agregar tienda", use_container_width=True):
            grafo_activo.agregar_tienda(nueva_tienda)
            st.success("Tienda agregada al mapa del sistema")
            
    with col2:
        st.markdown("#### Agregar Ruta")
        origen = st.text_input("Origen", placeholder="Tienda origen", key="origen")
        destino = st.text_input("Destino", placeholder="Tienda destino", key="destino")
        distancia = st.number_input("Distancia (km)", min_value=1, step=1)
        if st.button("Agregar ruta", use_container_width=True):
            grafo_activo.agregar_ruta(origen, destino, distancia)
            st.success("Ruta conectada correctamente")
            
    st.markdown("### Calcular Ruta Más Corta")
    col3, col4 = st.columns(2)
    with col3:
        origen_corto = st.text_input("Origen", placeholder="Tienda origen", key="origen_corto")
    with col4:
        destino_corto = st.text_input("Destino", placeholder="Tienda destino", key="destino_corto")
        
    if st.button("Calcular camino más corto", use_container_width=True):
        grafo_activo.camino_mas_corto(origen_corto, destino_corto)
        
    st.markdown("### Información del Grafo")
    if st.button("Mostrar componentes conexas", use_container_width=True):
        grafo_activo.componentes_conexos()

with tab3:
    st.markdown("### Estadísticas de Pedidos")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Pedidos pendientes", use_container_width=True):
            sistema.pedidos_pendientes()
    with col2:
        if opcion != "Lista Enlazada" and st.button("Altura del árbol", use_container_width=True):
            sistema.altura()
            
    if opcion != "Lista Enlazada":
        st.markdown("### Buscar por Rango")
        col3, col4 = st.columns(2)
        with col3:
            rango_min = st.number_input("Desde", min_value=1, step=1, key="rango_min")
        with col4:
            rango_max = st.number_input("Hasta", min_value=1, step=1, key="rango_max")
        if st.button("Buscar en rango", use_container_width=True):
            sistema.pedidos_en_rango(rango_min, rango_max)
            
    if opcion == "Lista Enlazada":
        st.markdown("### Actualizar Fecha")
        num_fecha = st.number_input("Número de pedido", min_value=1, step=1, key="num_fecha")
        nueva_fecha = st.text_input("Nueva fecha", placeholder="AAAA-MM-DD")
        if st.button("Actualizar fecha", use_container_width=True):
            sistema.actualizar_fecha_entrega(num_fecha, nueva_fecha)
