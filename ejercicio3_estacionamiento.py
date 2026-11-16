# ==============================================================
# Archivo:      ejercicio3_estacionamiento.py
# Curso:        SOFT-01 Principios de Programación 1
# Autor:        Miguel Vargas
# Fecha:        2026-11-15
# Versión:      1.0
# Descripción:  Sistema de consola para un estacionamiento de 20
#               espacios. Menú repetitivo con while True y
#               condicional múltiple para registrar ingresos,
#               salidas con cobro por hora y consultas.
# ==============================================================

# --- Constantes ---
CAPACIDAD_MAXIMA = 20
TARIFA_POR_HORA = 800  # colones

# --- Estado inicial de la sesión ---
vehiculos_presentes = 0
salidas_registradas = 0
recaudacion_total = 0

# --- Menú repetitivo ---
while True:
    print("===== ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        # Solo se suma si queda al menos un espacio
        if vehiculos_presentes < CAPACIDAD_MAXIMA:
            vehiculos_presentes = vehiculos_presentes + 1
            print(f"Ingreso registrado. Vehículos dentro: {vehiculos_presentes}")
        else:
            print("Estacionamiento lleno. No se puede registrar el ingreso.")

    elif opcion == "2":
        # Primero se verifica que haya carros; si no, ni se piden horas
        if vehiculos_presentes == 0:
            print("No hay vehículos dentro del estacionamiento.")
        else:
            horas_texto = input("Horas a cobrar: ").strip()
            # isdigit() descarta texto, negativos y decimales
            while not horas_texto.isdigit() or int(horas_texto) == 0:
                print("  Las horas deben ser un número entero mayor que 0.")
                horas_texto = input("Horas a cobrar: ").strip()

            horas_cobradas = int(horas_texto)
            monto_pago = horas_cobradas * TARIFA_POR_HORA

            vehiculos_presentes = vehiculos_presentes - 1
            salidas_registradas = salidas_registradas + 1
            recaudacion_total = recaudacion_total + monto_pago
            print(f"Salida registrada. Monto a pagar: ₡{monto_pago}")

    elif opcion == "3":
        espacios_libres = CAPACIDAD_MAXIMA - vehiculos_presentes
        print(f"Espacios ocupados: {vehiculos_presentes}")
        print(f"Espacios libres:   {espacios_libres}")

    elif opcion == "4":
        print(f"Recaudación total: ₡{recaudacion_total}")
        print(f"Vehículos que han salido: {salidas_registradas}")

    elif opcion == "5":
        print("--- Resumen final de la sesión ---")
        print(f"Vehículos dentro:   {vehiculos_presentes}")
        print(f"Salidas procesadas: {salidas_registradas}")
        print(f"Recaudación total:  ₡{recaudacion_total}")
        break  # única forma de salir del menú

    else:
        print("Opción inválida. Intente de nuevo.")
