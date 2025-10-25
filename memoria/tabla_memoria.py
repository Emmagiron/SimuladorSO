# memoria/tabla_memoria.py
# 🧠 Gestión de particiones de memoria: Best-Fit, liberación y visualización

def best_fit(particiones, proceso_id, tamano):
    """Asigna el proceso a la mejor partición disponible usando Best-Fit."""
    mejor = None
    for p in particiones:
        if p["proceso"] == "Libre" and p["tamano"] >= tamano:
            if mejor is None or p["tamano"] < mejor["tamano"]:
                mejor = p
    if mejor:
        mejor["proceso"] = proceso_id
        mejor["fragmentacion"] = mejor["tamano"] - tamano
        return True
    return False

def liberar_proceso(particiones, proceso_id):
    """Libera la partición ocupada por el proceso dado."""
    liberado = False
    for p in particiones:
        if p["proceso"] == proceso_id:
            p["proceso"] = "Libre"
            p["fragmentacion"] = 0
            liberado = True
            print(f"🧹 Partición '{p['id']}' liberada del proceso {proceso_id}.")
    if not liberado:
        print(f"⚠️ No se encontró ninguna partición ocupada por el proceso {proceso_id}.")

def mostrar_tabla(particiones):
    """Devuelve una tabla textual con el estado actual de las particiones."""
    tabla = "\n📊 Tabla de Particiones de Memoria\n"
    tabla += "╔════════════╦══════════╦══════════╦══════════╦════════════════╗\n"
    tabla += "║ Partición  ║  Inicio  ║  Tamaño  ║ Proceso  ║ Fragmentación  ║\n"
    tabla += "╠════════════╬══════════╬══════════╬══════════╬════════════════╣\n"

    for p in particiones:
        id_part = f"{p['id']:<10}"                     # izquierda, ancho 10
        inicio = f"{p['inicio']:>8}K"                  # derecha, ancho 8
        tamano = f"{p['tamano']:>8}K"                  # derecha, ancho 8
        proceso = f"{p['proceso']:<8}"                 # izquierda, ancho 8
        frag = f"{p['fragmentacion']:>12}K"            # derecha, ancho 12

        tabla += f"║ {id_part} ║ {inicio} ║ {tamano} ║ {proceso} ║ {frag} ║\n"

    tabla += "╚════════════╩══════════╩══════════╩══════════╩════════════════╝\n"
    return tabla
