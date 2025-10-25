# 📈 Cálculo de métricas finales: retorno, espera, promedios y rendimiento

def calcular_estadisticas(procesos, tiempo_total):
    print("\n📊 Estadísticas Finales")
    total_retorno = 0
    total_espera = 0
    terminados = 0

    print("ID | Arribo | Irrupción | Fin | Retorno | Espera")
    for p in procesos:
        if p["estado"] == "Terminado":
            fin = p.get("fin", p["arribo"] + p["irrupcion"])  # fallback
            retorno = fin - p["arribo"]
            espera = retorno - p["irrupcion"]
            total_retorno += retorno
            total_espera += espera
            terminados += 1
            print(f"{p['id']:3} | {p['arribo']:6} | {p['irrupcion']:9} | {fin:3} | {retorno:7} | {espera:6}")
        else:
            print(f"{p['id']:3} | No terminado")

    if terminados > 0:
        print(f"\n📌 Promedio de Retorno: {total_retorno / terminados:.2f}")
        print(f"📌 Promedio de Espera: {total_espera / terminados:.2f}")
        print(f"📌 Rendimiento del sistema: {terminados / tiempo_total:.2f} procesos por unidad de tiempo")
    else:
        print("⚠️ No se terminó ningún proceso.")
