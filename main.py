# 🚀 Simulador Paso a Paso de Asignación de Memoria y Planificación de Procesos

from memoria.particiones import crear_particiones
from memoria.tabla_memoria import best_fit, liberar_proceso, mostrar_tabla
from procesos.gestor_procesos import cargar_procesos
from planificador.srtf import seleccionar_siguiente, avanzar_tiempo
from salida.estadisticas import calcular_estadisticas
from salida.presentacion import mostrar_estado
from config.parametros import RUTA_PROCESOS, GRADO_MULTIPROGRAMACION

class SimuladorPasoAPaso:
    def __init__(self):
        self.particiones = crear_particiones()
        self.procesos = cargar_procesos(RUTA_PROCESOS)
        self.tiempo = 0
        self.procesador = None
        self.finalizado = False
        self.log = "📦 Simulación iniciada...\n"

    def contar_en_memoria(self):
        return sum(1 for p in self.procesos if p["estado"] in ["Listo", "Ejecución"])

    def paso(self):
        if self.finalizado:
            return "🎯 Simulación ya finalizada.\n"

        log_tick = f"\n{'═'*40}\n🕒 Tiempo actual: {self.tiempo}\n"

        # 🆕 Llegada de nuevos procesos
        for p in self.procesos:
            if p["arribo"] == self.tiempo and p["estado"] == "Nuevo":
                if self.contar_en_memoria() < GRADO_MULTIPROGRAMACION:
                    if best_fit(self.particiones, p["id"], p["tamano"]):
                        p["estado"] = "Listo"
                        log_tick += f"🆕 Proceso {p['id']} llegó y fue asignado a memoria.\n"
                    else:
                        p["estado"] = "Listo Suspendido"
                        log_tick += f"⏳ Proceso {p['id']} llegó pero no hay partición disponible.\n"
                else:
                    p["estado"] = "Listo Suspendido"
                    log_tick += f"⏳ Proceso {p['id']} llegó pero se alcanzó el grado de multiprogramación.\n"

        # 🔄 Intentar reactivar suspendidos
        for p in self.procesos:
            if p["estado"] == "Listo Suspendido":
                if self.contar_en_memoria() < GRADO_MULTIPROGRAMACION:
                    if best_fit(self.particiones, p["id"], p["tamano"]):
                        p["estado"] = "Listo"
                        log_tick += f"🔄 Proceso {p['id']} reactivado desde suspendido y asignado a memoria.\n"

        # ⚙️ Selección de proceso a ejecutar
        siguiente = seleccionar_siguiente(self.procesos, self.tiempo)
        if siguiente:
            if self.procesador is None or siguiente["id"] != self.procesador["id"]:
                self.procesador = siguiente
                self.procesador["estado"] = "Ejecución"
                log_tick += f"⚙️ Ejecutando proceso {self.procesador['id']}\n"
            else:
                log_tick += f"🔁 Continuando ejecución de proceso {self.procesador['id']}\n"

        # 📋 Estado del sistema
        log_tick += mostrar_estado(self.tiempo, self.procesador, self.procesos)
        log_tick += mostrar_tabla(self.particiones)

        # ⏳ Avanzar tiempo de ejecución
        if self.procesador is not None:
            self.procesador = avanzar_tiempo(self.procesador, self.procesos, self.tiempo)
            if self.procesador and self.procesador["restante"] == 0:
                log_tick += f"✅ Proceso {self.procesador['id']} terminado. Liberando memoria...\n"
                liberar_proceso(self.particiones, self.procesador["id"])
                self.procesador["estado"] = "Terminado"
                self.procesador["fin"] = self.tiempo
                self.procesador = None

                # 🔄 Intentar reactivar suspendidos tras liberación
                for p in self.procesos:
                    if p["estado"] == "Listo Suspendido":
                        if self.contar_en_memoria() < GRADO_MULTIPROGRAMACION:
                            if best_fit(self.particiones, p["id"], p["tamano"]):
                                p["estado"] = "Listo"
                                log_tick += f"🔄 Proceso {p['id']} reactivado desde suspendido y asignado a memoria.\n"
        else:
            log_tick += "⏸️ Procesador libre y sin procesos listos.\n"

        # 🛑 Verificar fin de simulación
        if self.procesador is None and not any(p["estado"] == "Listo" for p in self.procesos):
            log_tick += "🚨 Simulación estancada: no hay procesos listos ni en ejecución.\n"
            calcular_estadisticas(self.procesos, self.tiempo)
            no_terminados = [p["id"] for p in self.procesos if p["estado"] != "Terminado"]
            if no_terminados:
                log_tick += f"\n⚠️ Procesos no terminados: {', '.join(no_terminados)}\n"
            log_tick += f"\n🎯 Simulación finalizada en tiempo {self.tiempo} 🔋🔋.\n"
            self.finalizado = True

        self.tiempo += 1
        self.log += log_tick
        return log_tick
