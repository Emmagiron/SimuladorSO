# 🎬 Presentación del estado del sistema en cada tick

def mostrar_estado(tiempo, procesador, procesos):
    """Devuelve una presentación visual del estado del sistema en el tiempo actual."""
    estado = f"\n📋 Estado del Sistema - Tiempo {tiempo}\n"
    estado += "╔════════════════════════════════════════╗\n"

    # ⚙️ Estado del procesador
    if procesador:
        estado += f"║ ⚙️ Procesador ejecutando: {procesador['id']} (restante: {procesador['restante']})\n"
    else:
        estado += "║ ⚙️ Procesador libre\n"

    # 📥 Cola de procesos listos
    cola_listos = [p["id"] for p in procesos if p["estado"] == "Listo"]
    estado += f"║ 📥 Cola de Listos: {', '.join(cola_listos) if cola_listos else 'Vacía'}\n"

    # 📦 Cola de procesos suspendidos
    cola_suspendidos = [p["id"] for p in procesos if p["estado"] == "Listo Suspendido"]
    estado += f"║ 📦 Listos Suspendidos: {', '.join(cola_suspendidos) if cola_suspendidos else 'Vacía'}\n"

    estado += "╚════════════════════════════════════════╝\n"
    return estado
