-----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
BREVE DESCRIPCION DEL SIMULADOR
Este simulador permite visualizar y comprender el ciclo de vida completo de los procesos en un sistema con planificación a corto plazo y asignación de memoria por particiones fijas. Está diseñado para funcionar en un entorno de un solo procesador, respetando un grado de multiprogramación de 5 y aplicando las siguientes políticas:

Asignación de memoria: Best-Fit sobre particiones fijas (100K SO, 250K grandes, 150K medianos, 50K pequeños).

Planificación de CPU: Algoritmo SRTF (Shortest Remaining Time First).

Gestión de estados: Nuevo, Listo, Listo Suspendido, Ejecución y Terminado.

El simulador permite cargar hasta 10 procesos desde archivo, mostrar el estado del procesador, la tabla de memoria, las colas de procesos y generar estadísticas finales como tiempos de espera, retorno y rendimiento del sistema.

Está implementado en Python con estructura modular, pensado para facilitar el análisis, la presentación didáctica y el trabajo colaborativo en equipos.
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
Requisitos para correrlo.


Créditos del equipo.