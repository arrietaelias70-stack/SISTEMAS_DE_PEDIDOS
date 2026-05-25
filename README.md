# Sistema de Gestión de Pedidos y Rutas de Entrega

## Integrantes

Elias David Arrieta Olivero – 2250952  

Emanuel Miranda Sinning – 2250913  

Mario Jose Moreno Ramirez – 2250941  

Miguel Angel Plata Tello – 2211245  

Gabriel Alejandro Zambrano Herazo – 2250944  

Daniel Esteban Romero Dueñes – 2250948  

---

# Resumen General del Proyecto

El propósito principal de este proyecto fue desarrollar un sistema de gestión de pedidos y optimización de rutas de entrega utilizando diferentes estructuras de datos en Python. A lo largo de todas las entregas se trabajó sobre una misma problemática: la administración eficiente de pedidos dentro de una red de tiendas conectadas entre sí, donde era necesario almacenar información, organizarla correctamente, realizar búsquedas rápidas y optimizar recorridos de entrega dentro de la infraestructura.

El proyecto fue evolucionando progresivamente durante cada avance. Inicialmente se trabajó con estructuras lineales sencillas y posteriormente se incorporaron modelos más complejos que permitieron mejorar considerablemente el rendimiento del sistema y representar de forma mucho más realista el contexto del problema planteado.

Más allá de implementar únicamente código funcional, el proyecto permitió entender cómo la elección de una estructura de datos influye directamente en la eficiencia de un sistema, especialmente cuando aumenta el volumen de información o la cantidad de conexiones existentes dentro de una red.

---

# Primera Etapa: Implementación con Listas Enlazadas

En el primer avance se desarrolló una infraestructura basada en listas enlazadas simples utilizando programación orientada a objetos. Cada pedido era almacenado dentro de un nodo conectado dinámicamente con el siguiente, permitiendo manejar información sin depender de tamaños fijos en memoria.

Durante esta etapa el sistema permitió registrar pedidos, eliminarlos, recorrer la información almacenada y realizar búsquedas básicas dentro de la estructura. La implementación fue útil para comprender el funcionamiento de estructuras dinámicas y establecer la base inicial del proyecto.

El uso de listas enlazadas permitió que el sistema creciera de manera flexible, evitando desperdicio de memoria y facilitando la inserción de nuevos pedidos. Sin embargo, a medida que aumentaba la cantidad de datos comenzaron a aparecer limitaciones importantes relacionadas con el tiempo de búsqueda, ya que el sistema debía recorrer secuencialmente cada nodo hasta encontrar la información solicitada.

Aunque esta primera solución era funcional, resultaba evidente que el rendimiento podía mejorarse considerablemente utilizando estructuras más eficientes para búsquedas y organización automática de información.

---

# Segunda Etapa: Implementación con Árboles BST

En el segundo avance se implementaron árboles binarios de búsqueda BST con el objetivo de optimizar el acceso y organización de los pedidos dentro del sistema. Gracias a esta estructura, los pedidos comenzaron a almacenarse jerárquicamente, permitiendo búsquedas más rápidas y una administración más eficiente frente al crecimiento de información.

Durante esta etapa se desarrollaron funcionalidades de inserción automática, búsquedas optimizadas, generación de reportes ordenados mediante recorridos inorden y consultas por rangos de pedidos. Estas mejoras permitieron reducir considerablemente los recorridos innecesarios y mejorar el rendimiento general del sistema en comparación con la implementación basada en listas enlazadas.

Además, se integró un motor de búsqueda recursivo sobre el árbol BST y se implementaron métodos de organización automática que mantenían estructurados los pedidos desde el momento de su inserción. El código completo de estas implementaciones se encuentra disponible dentro del repositorio del proyecto.

---

# Etapa Final: Implementación con Grafos

En la etapa final se integró una estructura basada en grafos ponderados para representar de manera más realista las conexiones entre tiendas y rutas de entrega. Cada tienda fue modelada como un nodo y cada conexión como una ruta con costos asociados, permitiendo simular una red de distribución mucho más cercana a un entorno logístico real.

Durante esta implementación se desarrollaron funcionalidades relacionadas con inserción de tiendas, eliminación de conexiones, búsqueda de rutas y optimización de recorridos dentro de la red. También se incorporaron algoritmos capaces de calcular rutas más eficientes entre distintos puntos del sistema, mejorando la administración de entregas y el análisis de conexiones disponibles.

La integración de grafos representó la etapa más completa del proyecto, ya que permitió combinar administración de información, organización de pedidos y optimización de rutas dentro de una misma solución. El código detallado de esta implementación puede consultarse directamente en el repositorio del proyecto.

---

# Funcionalidades Implementadas

A lo largo del desarrollo del proyecto se incorporaron distintas funcionalidades que fueron evolucionando en cada entrega. Entre las principales capacidades del sistema se encuentran el registro dinámico de pedidos, búsqueda de información, organización automática mediante árboles BST, generación de reportes ordenados, consultas por rango, administración de conexiones entre tiendas y cálculo de rutas eficientes dentro de la red de distribución.

Cada implementación tuvo como objetivo mejorar el comportamiento del sistema frente al crecimiento de información y aumentar la capacidad de representación del problema trabajado.

---

# Comparación Entre las Estructuras Utilizadas

| Estructura | Comportamiento dentro del sistema |
|---|---|
| Lista enlazada | Permitió manejar pedidos dinámicamente, aunque las búsquedas aumentaban linealmente con la cantidad de información |
| Árbol BST | Mejoró significativamente la velocidad de búsqueda y la organización automática de los pedidos |
| Grafo ponderado | Permitió representar rutas reales, múltiples conexiones y optimización de recorridos dentro de la red |

Esta evolución permitió observar claramente cómo cada estructura aporta ventajas específicas dependiendo del contexto y del tipo de problema que se desea resolver.

---

# Análisis Técnico del Proyecto

Desde el punto de vista técnico, el proyecto no se enfocó únicamente en implementar estructuras aisladas, sino en construir una infraestructura completa capaz de integrar diferentes soluciones dentro de un mismo sistema.

El verdadero valor del desarrollo realizado radica en cómo cada etapa fue resolviendo limitaciones presentes en la anterior. Las listas enlazadas ofrecieron flexibilidad inicial, los árboles BST optimizaron búsquedas y organización de datos, mientras que los grafos permitieron modelar escenarios logísticos mucho más complejos y cercanos a situaciones reales.

A nivel computacional, el proyecto permitió reducir recorridos innecesarios, mejorar tiempos de respuesta y optimizar el manejo de información dentro del sistema. Además, todas las implementaciones fueron desarrolladas utilizando programación orientada a objetos, facilitando la organización del código y la reutilización de funcionalidades.

---

# Conclusiones

El desarrollo de este proyecto permitió evolucionar progresivamente desde estructuras lineales simples hasta modelos avanzados orientados a optimización de rutas y representación de redes complejas.

Cada etapa aportó mejoras importantes dentro del sistema y permitió comprender de manera práctica cómo las estructuras de datos influyen directamente en el rendimiento de una aplicación.

Las listas enlazadas facilitaron la construcción inicial del sistema y el manejo dinámico de pedidos. Posteriormente, los árboles BST permitieron optimizar búsquedas, organización automática y generación de reportes ordenados. Finalmente, los grafos proporcionaron una representación mucho más eficiente para el contexto trabajado, permitiendo administrar conexiones entre tiendas y calcular rutas óptimas dentro de la infraestructura.

Después de analizar el comportamiento de cada implementación, se concluyó que los grafos representan la solución más eficiente para la problemática planteada, debido a que permiten modelar redes reales de distribución, gestionar múltiples conexiones y optimizar recorridos de entrega de manera mucho más precisa.

Además del desarrollo técnico, el proyecto fortaleció conocimientos relacionados con estructuras de datos, algoritmos, programación orientada a objetos, Git, GitHub y trabajo colaborativo dentro de un entorno de desarrollo.

---

# Tecnologías Utilizadas

Python  

Git  

GitHub  

Programación Orientada a Objetos  

Árboles Binarios de Búsqueda BST  

Grafos Ponderados  

---

# Repositorio del Proyecto

https://github.com/arrietaelias70-stack/SISTEMAS_DE_PEDIDOS
