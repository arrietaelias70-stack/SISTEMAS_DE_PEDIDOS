import sqlite3

def obtener_conexion():
    return sqlite3.connect("pedidos.db")

def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pedidos (numero INTEGER PRIMARY KEY, tienda TEXT, productos TEXT, estado TEXT)")
    conexion.commit()
    conexion.close()

def guardar(numero, tienda, productos, estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT OR REPLACE INTO pedidos VALUES (?, ?, ?, ?)", (numero, tienda, productos, estado))
    conexion.commit()
    conexion.close()

def eliminar(numero):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pedidos WHERE numero = ?", (numero,))
    conexion.commit()
    conexion.close()

def eliminar_todos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pedidos")
    conexion.commit()
    conexion.close()

def obtener_todos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT numero, tienda, productos, estado FROM pedidos")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def obtener_por_numero(numero):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT numero, tienda, productos, estado FROM pedidos WHERE numero = ?", (numero,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

def actualizar_estado(numero, nuevo_estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE pedidos SET estado = ? WHERE numero = ?", (nuevo_estado, numero))
    conexion.commit()
    conexion.close()

def contar_pedidos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos")
    resultado = cursor.fetchone()[0]
    conexion.close()
    return resultado

def contar_por_estado(estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE estado = ?", (estado,))
    resultado = cursor.fetchone()[0]
    conexion.close()
    return resultado

def obtener_por_tienda(tienda):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT numero, tienda, productos, estado FROM pedidos WHERE tienda = ?", (tienda,))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def obtener_en_rango(min_num, max_num):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT numero, tienda, productos, estado FROM pedidos WHERE numero BETWEEN ? AND ?", (min_num, max_num))
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

crear_tabla()