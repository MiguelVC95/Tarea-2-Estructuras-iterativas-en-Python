# ==============================================================
# Archivo:      ejercicio4_expedicion.py
# Curso:        SOFT-01 Principios de Programación 1
# Autor:        Miguel Vargas
# Fecha:        2026-11-15
# Versión:      1.0
# Descripción:  Simula las jornadas de una expedición con 150 L de
#               agua y 100 unidades de alimento. Valida consumos,
#               descuenta recursos y detiene la misión con break
#               si algún recurso se agota con jornadas pendientes.
# ==============================================================

# --- Constantes ---
AGUA_INICIAL = 150.0
ALIMENTO_INICIAL = 100.0
JORNADAS_MINIMAS = 1
JORNADAS_MAXIMAS = 30

print("=== Control de abastecimiento de la expedición ===")

# --- Entrada: cantidad de jornadas validada ---
jornadas_texto = input(f"Cantidad de jornadas ({JORNADAS_MINIMAS}-{JORNADAS_MAXIMAS}): ").strip()
while (not jornadas_texto.isdigit()
       or int(jornadas_texto) < JORNADAS_MINIMAS
       or int(jornadas_texto) > JORNADAS_MAXIMAS):
    print(f"  Debe ser un entero entre {JORNADAS_MINIMAS} y {JORNADAS_MAXIMAS}.")
    jornadas_texto = input(f"Cantidad de jornadas ({JORNADAS_MINIMAS}-{JORNADAS_MAXIMAS}): ").strip()
cantidad_jornadas = int(jornadas_texto)

# --- Inicialización ---
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL
agua_consumida = 0.0
alimento_consumido = 0.0
dias_completados = 0
expedicion_interrumpida = False

# --- Iteración por jornadas ---
for dia in range(1, cantidad_jornadas + 1):
    # Al iniciar la jornada se revisa si queda de ambos recursos.
    # Solo se llega aquí si hay días pendientes, así que el break
    # corta la misión antes de tiempo.
    if agua_disponible == 0 or alimento_disponible == 0:
        expedicion_interrumpida = True
        break

    print(f"--- Jornada {dia} de {cantidad_jornadas} ---")
    print(f"Disponible: {agua_disponible:.1f} L de agua | {alimento_disponible:.1f} u. de alimento")

    # Validación del agua: positiva y sin exceder lo disponible
    consumo_agua = float(input("Agua consumida (L): "))
    while consumo_agua <= 0 or consumo_agua > agua_disponible:
        print(f"  Inválido: debe ser mayor que 0 y no superar {agua_disponible:.1f} L.")
        consumo_agua = float(input("Agua consumida (L): "))

    # Validación del alimento: misma regla
    consumo_alimento = float(input("Alimento consumido (u.): "))
    while consumo_alimento <= 0 or consumo_alimento > alimento_disponible:
        print(f"  Inválido: debe ser mayor que 0 y no superar {alimento_disponible:.1f} u.")
        consumo_alimento = float(input("Alimento consumido (u.): "))

    # Se redondea para evitar errores de precisión de los float (ej. 0.0000001)
    agua_disponible = round(agua_disponible - consumo_agua, 2)
    alimento_disponible = round(alimento_disponible - consumo_alimento, 2)
    agua_consumida = agua_consumida + consumo_agua
    alimento_consumido = alimento_consumido + consumo_alimento
    dias_completados = dias_completados + 1

    print(f"Saldo: {agua_disponible:.1f} L de agua | {alimento_disponible:.1f} u. de alimento")

# --- Proceso final ---
promedio_agua = 0.0
promedio_alimento = 0.0
if dias_completados > 0:
    promedio_agua = agua_consumida / dias_completados
    promedio_alimento = alimento_consumido / dias_completados

if not expedicion_interrumpida:
    estado_expedicion = "Completada"
elif agua_disponible == 0 and alimento_disponible == 0:
    estado_expedicion = "Interrumpida: se agotaron agua y alimento"
elif agua_disponible == 0:
    estado_expedicion = "Interrumpida: se agotó el agua"
else:
    estado_expedicion = "Interrumpida: se agotó el alimento"

# --- Salida ---
print("===== Informe de la expedición =====")
print(f"Días completados:        {dias_completados} de {cantidad_jornadas}")
print(f"Agua consumida:          {agua_consumida:.1f} L")
print(f"Alimento consumido:      {alimento_consumido:.1f} u.")
print(f"Agua restante:           {agua_disponible:.1f} L")
print(f"Alimento restante:       {alimento_disponible:.1f} u.")
print(f"Promedio diario agua:    {promedio_agua:.2f} L")
print(f"Promedio diario alimento:{promedio_alimento:.2f} u.")
print(f"Estado:                  {estado_expedicion}")
