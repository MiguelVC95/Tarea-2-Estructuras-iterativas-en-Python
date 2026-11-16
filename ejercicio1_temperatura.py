# ==============================================================
# Archivo:      ejercicio1_temperatura.py
# Curso:        SOFT-01 Principios de Programación 1
# Autor:        Miguel Vargas
# Fecha:        2026-11-15
# Versión:      1.0
# Descripción:  Simula el calentamiento de una cámara experimental.
#               Recibe la temperatura inicial, la objetivo y el
#               incremento por ciclo. Si la configuración es válida,
#               calienta con un while hasta alcanzar o superar el
#               objetivo y muestra cada ciclo.
# ==============================================================

print("=== Control de temperatura - Cámara experimental ===")

# --- Entrada ---
temperatura_inicial = float(input("Temperatura inicial (°C): "))
temperatura_objetivo = float(input("Temperatura objetivo (°C): "))
incremento = float(input("Incremento por ciclo (°C): "))

# --- Validación de la configuración ---
# Si algo no cumple, se informa el motivo y no se simula
if temperatura_objetivo <= temperatura_inicial:
    print("Configuración inválida: la temperatura objetivo debe ser mayor que la inicial.")
elif incremento <= 0:
    print("Configuración inválida: el incremento debe ser mayor que 0 °C.")
else:
    # --- Proceso: simulación del calentamiento ---
    temperatura_actual = temperatura_inicial
    ciclos = 0

    # Se usa while porque no se sabe de antemano cuántos ciclos hacen falta
    while temperatura_actual < temperatura_objetivo:
        temperatura_actual = temperatura_actual + incremento  # actualiza la variable de control
        ciclos = ciclos + 1
        print(f"Ciclo {ciclos}: {temperatura_actual:.1f} °C")

    # --- Salida ---
    print("--- Resultado de la sesión ---")
    print(f"Temperatura alcanzada: {temperatura_actual:.1f} °C")
    print(f"Total de ciclos: {ciclos}")
