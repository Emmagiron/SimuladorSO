from config.parametros import PARTICIONES

def crear_particiones():
    """Inicializa las particiones de memoria según configuración fija."""
    particiones = []
    inicio = 0

    for p in PARTICIONES:
        particiones.append({
            "id": p["id"],                          # Nombre de la partición
            "inicio": inicio,                       # Dirección de inicio en memoria
            "tamano": p["tamano"],                  # Tamaño total de la partición
            "proceso": "Sistema" if p["id"] == "SO" else "Libre",  # Estado inicial
            "fragmentacion": 0                      # Fragmentación interna
        })
        inicio += p["tamano"]                       # Avanzar dirección para la siguiente

    return particiones
