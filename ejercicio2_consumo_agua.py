# ==============================================================
# Archivo:      ejercicio2_consumo_agua.py
# Curso:        SOFT-01 Principios de Programación 1
# Autor:        Miguel Vargas
# Fecha:        2026-11-15
# Versión:      1.0
# Descripción:  Registra el consumo de agua de 7 días con un ciclo
#               for y calcula total, promedio, consumo máximo y
#               cantidad de días que superan 150 L, sin usar
#               listas ni las funciones sum() o max().
# ==============================================================

# --- Constantes ---
DIAS_SEMANA = 7
UMBRAL_LITROS = 150

# --- Inicialización de acumulador, contador y máximo ---
consumo_total = 0.0
consumo_maximo = 0.0
dias_sobre_umbral = 0

print("=== Registro semanal de consumo de agua ===")

# --- Iteración: se conoce la cantidad de días, por eso for + range() ---
for dia in range(1, DIAS_SEMANA + 1):
    consumo_dia = float(input(f"Consumo del día {dia} (L): "))

    # Validación: no se aceptan consumos negativos
    while consumo_dia < 0:
        print("  El consumo no puede ser negativo. Intente de nuevo.")
        consumo_dia = float(input(f"Consumo del día {dia} (L): "))

    consumo_total = consumo_total + consumo_dia

    # El primer día siempre es el máximo inicial; después se compara
    if dia == 1 or consumo_dia > consumo_maximo:
        consumo_maximo = consumo_dia

    # Estrictamente mayor: 150 L exactos no cuentan
    if consumo_dia > UMBRAL_LITROS:
        dias_sobre_umbral = dias_sobre_umbral + 1

# --- Proceso final ---
promedio_diario = consumo_total / DIAS_SEMANA

# --- Salida ---
print("--- Resumen semanal ---")
print(f"Consumo total:        {consumo_total:.2f} L")
print(f"Promedio diario:      {promedio_diario:.2f} L")
print(f"Mayor consumo:        {consumo_maximo:.2f} L")
print(f"Días sobre {UMBRAL_LITROS} L:     {dias_sobre_umbral}")
