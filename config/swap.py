# config/swap.py

procesos_en_memoria = []
procesos_en_disco = []

def swap_out():
    if procesos_en_memoria:
        proceso = procesos_en_memoria.pop(0)
        procesos_en_disco.append(proceso)
        print(f"📤 Swap-out: {get_nombre(proceso)}")

def swap_in():
    if procesos_en_disco:
        proceso = procesos_en_disco.pop(0)
        procesos_en_memoria.append(proceso)
        print(f"📥 Swap-in: {get_nombre(proceso)}")

def gestionar_swap():
    swap_in()
    if procesos_en_memoria:
        proceso = procesos_en_memoria.pop()
        if proceso not in procesos_en_disco:
            procesos_en_disco.append(proceso)
            print(f"📤 Swap-out: {get_nombre(proceso)}")

def get_nombre(proceso):
    return proceso["id"] if isinstance(proceso, dict) else getattr(proceso, "nombre", "SinNombre")
