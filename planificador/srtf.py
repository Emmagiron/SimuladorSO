# planificador/srtf.py
# 🧠 Planificador SRTF: Selección y avance de procesos

def seleccionar_siguiente(procesos, tiempo_actual):
    candidatos = [
        p for p in procesos
        if p["estado"] in ["Listo", "Ejecución"]
        and p["arribo"] <= tiempo_actual
        and p["restante"] > 0
    ]
    return min(candidatos, key=lambda p: p["restante"]) if candidatos else None

def avanzar_tiempo(procesador, procesos, tiempo_actual):
    if procesador:
        procesador["restante"] -= 1
    return procesador
