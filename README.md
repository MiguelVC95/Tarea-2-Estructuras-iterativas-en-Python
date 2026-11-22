# Tarea 2 — Estructuras iterativas en Python

Repositorio con la solución de la Tarea 2 del curso **Principios de Programación 1**.
Contiene cuatro programas de consola que resuelven problemas usando ciclos `while` y `for`,
y la documentación técnica con tablas de variables, diagramas de flujo y casos de prueba.

> Por indicación del docente, los laboratorios guiados no forman parte de esta entrega.

---

## Descripción

Se desarrollaron cuatro soluciones independientes basadas en situaciones operativas:

- Control de temperatura de una cámara experimental.
- Registro semanal de consumo de agua.
- Administración de un estacionamiento privado.
- Control de abastecimiento de una expedición.

Los dos primeros ejercicios practican la repetición básica. Los dos últimos combinan ciclos,
condicionales, validaciones de entrada, contadores y acumuladores.

Todos los ejercicios se resolvieron **sin funciones propias, sin colecciones (listas,
diccionarios, tuplas), sin programación orientada a objetos, sin bibliotecas externas y
sin usar `sum()` ni `max()`**, tal como lo pide la consigna.

---

## Objetivos

- Elegir entre `while` y `for` según exista una condición de continuación o una cantidad fija de repeticiones.
- Diseñar ciclos con inicialización, condición, actualización y salida correctas, evitando ciclos infinitos y errores de límites.
- Usar contadores, acumuladores y condicionales para obtener resultados verificables.
- Validar entradas, implementar menús repetitivos y controlar interrupciones anticipadas con `break`.
- Documentar y probar los algoritmos con los estándares del curso.

---

## Funcionalidades

| Programa | Estructura principal | Qué hace |
|---|---|---|
| `ejercicio1_temperatura.py` | `while` | Valida la configuración y simula el calentamiento ciclo por ciclo hasta alcanzar o superar la temperatura objetivo. |
| `ejercicio2_consumo_agua.py` | `for` + `range()` | Registra el consumo de 7 días y calcula total, promedio, consumo máximo y días que superan 150 L. |
| `ejercicio3_estacionamiento.py` | `while True` + `if/elif/else` | Menú para registrar ingresos y salidas, controlar la capacidad de 20 espacios y cobrar ₡800 por hora. |
| `ejercicio4_expedicion.py` | `for` + `while` + `break` | Simula las jornadas de una expedición, valida consumos de agua y alimento e interrumpe la misión si un recurso se agota. |

---

## Requisitos previos

- [Python 3](https://www.python.org/downloads/) (probado con Python 3.13).
- [Visual Studio Code](https://code.visualstudio.com/) con la extensión de Python (recomendado).
- Git, para clonar el repositorio.

Para verificar la versión de Python instalada:

    python --version

> En Windows puede que el comando sea `py` en lugar de `python`.

---

## Instrucciones de ejecución

**Paso 1.** Clonar el repositorio:

    git clone https://github.com/MiguelVC95/Tarea-2-Estructuras-iterativas-en-Python.git
    cd Tarea-2-Estructuras-iterativas-en-Python

**Paso 2.** Entrar a la carpeta de ejercicios y ejecutar el programa deseado:

    cd ejercicios
    python ejercicio1_temperatura.py
    python ejercicio2_consumo_agua.py
    python ejercicio3_estacionamiento.py
    python ejercicio4_expedicion.py

También se puede abrir cualquier archivo `.py` en Visual Studio Code y ejecutarlo con el
botón **Run Python File** (▶) en la esquina superior derecha.

---

## Estructura del repositorio

    Tarea-2-Estructuras-iterativas-en-Python/
    ├── Ejercicios/
    │   ├── ejercicio1_temperatura.py
    │   ├── ejercicio2_consumo_agua.py
    │   ├── ejercicio3_estacionamiento.py
    │   └── ejercicio4_expedicion.py
    ├── Documentacion/
    │   ├── Tarea2_Documentacion.pdf
    │   └── Diagramas/
    │       ├── ejercicio1_temperatura.drawio
    │       ├── ejercicio1_temperatura.png
    │       ├── ejercicio2_consumo_agua.drawio
    │       ├── ejercicio2_consumo_agua.png
    │       ├── ejercicio3_estacionamiento.drawio
    │       ├── ejercicio3_estacionamiento.png
    │       ├── ejercicio4_expedicion.drawio
    │       └── ejercicio4_expedicion.png
    └── README.md

---

## Documentación

El archivo `documentacion/Tarea2_Documentacion.pdf` incluye para cada ejercicio:

- Descripción del problema y decisiones de diseño.
- Tabla de variables (nombre, tipo de dato, descripción y clasificación).
- Diagrama de flujo.
- Casos de prueba con entradas, resultado esperado, resultado obtenido, estado y evidencia de ejecución.

Los diagramas de flujo se encuentran en la carpeta `documentacion/diagramas/` en dos formatos:

- **`.drawio`:** formato editable, se abre en [draw.io](https://app.diagrams.net).
- **`.png`:** imagen para visualización rápida.

---

## Estándares aplicados

- Variables en `snake_case` y constantes en `MAYÚSCULAS`.
- Indentación de 4 espacios y espacios alrededor de los operadores.
- Encabezado comentado en cada archivo (nombre, curso, autor, fecha, versión y descripción).
- Comentarios breves para identificar bloques de entrada, proceso, decisiones, iteración y salida.
- Sin números mágicos: los valores fijos se definen como constantes.

---

## Autor

**Miguel Angel Vargas Cedeño**
Estudiante de Ingeniería del Software
GitHub: [@MiguelVC95](https://github.com/MiguelVC95)

---

## Información académica

| Dato | Detalle |
|---|---|
| **Universidad** | Universidad CENFOTEC |
| **Escuela** | Escuela de Ingeniería del Software |
| **Curso** | SOFT-01 — Principios de Programación 1 |
| **Sección** | SCP0 |
| **Periodo** | 2026-C3 |
| **Docente** | Dario Rodríguez Obando |
| **Fecha de entrega** | 22 de noviembre de 2026 |

---

## Estado del proyecto

🟢 **Finalizado — versión 1.0**
