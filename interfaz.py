import tkinter as tk
from tkinter import ttk, messagebox
from main import SimuladorPasoAPaso
from config import swap  # Importar el módulo swap para acceder a procesos_en_disco

# 🧠 Inicializar simulador
simulador = SimuladorPasoAPaso()

# 🖼️ Ventana principal
root = tk.Tk()
root.title("Simulador de Memoria y Procesos")
root.geometry("1200x800")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="🧠 Simulador SRTF + Best-Fit (Paso a Paso)", font=("Arial", 16)).pack(pady=10)

# 📝 Área de texto para log
ttk.Label(frame, text="📜 Log de Simulación", font=("Arial", 12)).pack()
salida_area = tk.Text(frame, wrap="word", font=("Courier", 10), height=18)
salida_area.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=salida_area.yview)
scrollbar.pack(side="right", fill="y")
salida_area.config(yscrollcommand=scrollbar.set)

salida_area.insert("end", "📦 Simulación iniciada...\n")

# 🎛️ Botones
boton_frame = ttk.Frame(frame)
boton_frame.pack(pady=10)

ttk.Button(boton_frame, text="▶ Siguiente paso", command=lambda: avanzar()).pack(side="left", padx=10)
ttk.Button(boton_frame, text="🔄 Reiniciar", command=lambda: reiniciar()).pack(side="left", padx=10)
ttk.Button(boton_frame, text="📤 Exportar log", command=lambda: exportar()).pack(side="left", padx=10)

# 📊 Distribución horizontal de tablas
tablas_frame = ttk.Frame(frame)
tablas_frame.pack(fill="x", pady=10)

izquierda = ttk.Frame(tablas_frame)
izquierda.pack(side="left", fill="both", expand=True)

derecha = ttk.Frame(tablas_frame)
derecha.pack(side="right", fill="y")

# 📦 Particiones de Memoria
ttk.Label(izquierda, text="📦 Particiones de Memoria", font=("Arial", 12)).pack()
tabla_memoria = ttk.Treeview(izquierda, columns=("Inicio", "Tamaño", "Proceso", "Fragmentación"), show="headings", height=4)
tabla_memoria.pack(pady=5)

for col in tabla_memoria["columns"]:
    tabla_memoria.heading(col, text=col)
    tabla_memoria.column(col, anchor="center", width=120)

# 🧠 Estado de Procesos
ttk.Label(izquierda, text="🧠 Estado de Procesos", font=("Arial", 12)).pack()
tabla_procesos = ttk.Treeview(izquierda, columns=("Estado", "Restante", "Arribo", "Tamaño"), show="headings", height=3)
tabla_procesos.pack(pady=5)

tabla_procesos.heading("#0", text="ID")
tabla_procesos.column("#0", anchor="center", width=50)

for col in tabla_procesos["columns"]:
    tabla_procesos.heading(col, text=col)
    tabla_procesos.column(col, anchor="center", width=100)

# 📀 Procesos en Disco (Swap)
ttk.Label(derecha, text="📀 Procesos en Disco (Swap)", font=("Arial", 12)).pack()
tabla_swap = ttk.Treeview(derecha, columns=("Tamaño", "Arribo"), show="headings", height=6)
tabla_swap.pack(pady=5)

tabla_swap.heading("#0", text="ID")
tabla_swap.column("#0", anchor="center", width=50)

for col in tabla_swap["columns"]:
    tabla_swap.heading(col, text=col)
    tabla_swap.column(col, anchor="center", width=100)

# ▶ Avanzar un paso
def avanzar():
    resultado = simulador.paso()
    salida_area.insert("end", resultado)
    salida_area.see("end")

    # 🧼 Limpiar tablas
    tabla_memoria.delete(*tabla_memoria.get_children())
    tabla_procesos.delete(*tabla_procesos.get_children())
    tabla_swap.delete(*tabla_swap.get_children())

    # 🧠 Cargar particiones
    for p in simulador.particiones:
        tabla_memoria.insert("", "end", values=(
            f"{p['inicio']}K",
            f"{p['tamano']}K",
            p["proceso"],
            f"{p['fragmentacion']}K"
        ))

    # 🧠 Cargar procesos
    for p in simulador.procesos:
        tabla_procesos.insert("", "end", text=p["id"], values=(
            p["estado"],
            f"{p['restante']}K" if p["estado"] != "Terminado" else "✔",
            p["arribo"],
            f"{p['tamano']}K"
        ))

    # 📀 Cargar procesos en disco (swap)
    for p in swap.procesos_en_disco:
        tabla_swap.insert("", "end", text=p["id"], values=(
            f"{p['tamano']}K",
            p["arribo"]
        ))

# 🔄 Reiniciar simulación
def reiniciar():
    global simulador
    simulador = SimuladorPasoAPaso()
    salida_area.delete("1.0", "end")
    salida_area.insert("end", "📦 Simulación reiniciada...\n")
    tabla_memoria.delete(*tabla_memoria.get_children())
    tabla_procesos.delete(*tabla_procesos.get_children())
    tabla_swap.delete(*tabla_swap.get_children())

# 📤 Exportar log
def exportar():
    with open("log_simulacion.txt", "w", encoding="utf-8") as f:
        f.write(salida_area.get("1.0", "end"))
    messagebox.showinfo("Exportación", "Log guardado como log_simulacion.txt")

root.mainloop()
