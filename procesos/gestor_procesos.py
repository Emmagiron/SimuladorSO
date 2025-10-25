import csv

def cargar_procesos(ruta_archivo):
    procesos = []
    with open(ruta_archivo, newline='') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            proceso = {
                "id": fila["id"],
                "tamano": int(fila["tamano"]),
                "arribo": int(fila["arribo"]),
                "irrupcion": int(fila["irrupcion"]),
                "restante": int(fila["irrupcion"]),  # para SRTF
                "estado": "Nuevo",
                "fin": None  # ⏱️ para registrar tiempo de finalización
            }
            procesos.append(proceso)
    return procesos

def mostrar_procesos(procesos):
    print("\n📦 Procesos cargados:")
    print("ID | Tamaño | Arribo | Irrupción | Estado")
    for p in procesos:
        print(f"{p['id']:3} | {p['tamano']:6}K | {p['arribo']:6} | {p['irrupcion']:9} | {p['estado']:8}")
