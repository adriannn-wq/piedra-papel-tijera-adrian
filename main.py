"""
Proyecto Integrador: Piedra, Papel o Tijera - Edición Avanzada
Autor: Adrian Alejandro Ron Albarracin
Materia: Lógica de Programación
Docente: Lilian Marlene Aman Ramos
Universidad Internacional del Ecuador - UIDE
Fecha: 2026

Descripción:
  Sistema de juego interactivo que extiende el programa original
  incorporando: historial de partidas, niveles de dificultad,
  modo torneo (al mejor de N rondas), estadísticas avanzadas
  y persistencia de datos en archivo de texto.

Unidades integradas:
  Unidad 1 - Fundamentos: variables, tipos de datos, entrada/salida
  Unidad 2 - Condicionales: validación, lógica de juego
  Unidad 3 - Bucles: menú, repetición de rondas, torneo
  Unidad 4 - Funciones y organización: modularización del código
"""

import random
import datetime

# ─────────────────────────────────────────────
#  CONSTANTES GLOBALES
# ─────────────────────────────────────────────
OPCIONES = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
EMOJIS   = {"Piedra": "🪨", "Papel": "📄", "Tijera": "✂️"}
COMBINA_GANADORAS = {("Piedra", "Tijera"), ("Papel", "Piedra"), ("Tijera", "Papel")}
ARCHIVO_HISTORIAL = "historial_partidas.txt"


# ─────────────────────────────────────────────
#  UNIDAD 4 · FUNCIONES DE PRESENTACIÓN
# ─────────────────────────────────────────────
def separador(simbolo="=", largo=42):
    """Imprime una línea decorativa."""
    print(simbolo * largo)


def titulo(texto):
    """Muestra un título centrado con separadores."""
    separador()
    print(f"  {texto}")
    separador()


def mostrar_reglas():
    """Muestra las reglas del juego."""
    titulo("REGLAS DEL JUEGO")
    print("  🪨  Piedra  vence a  ✂️  Tijera")
    print("  ✂️  Tijera  vence a  📄  Papel")
    print("  📄  Papel   vence a  🪨  Piedra")
    print()
    print("  Juega contra la computadora.")
    print("  En modo torneo gana quien llega")
    print("  primero al número de victorias.")
    separador()


# ─────────────────────────────────────────────
#  UNIDAD 1 · ENTRADA Y VALIDACIÓN
# ─────────────────────────────────────────────
def pedir_jugada():
    """Solicita y valida la jugada del usuario (Unidad 2: condicionales)."""
    while True:
        print("\n  Elige tu jugada:")
        for clave, nombre in OPCIONES.items():
            print(f"    {clave}. {EMOJIS[nombre]}  {nombre}")
        opcion = input("  → Escribe 1, 2 o 3: ").strip()
        if opcion in OPCIONES:
            return OPCIONES[opcion]
        print("  ⚠️  Opción no válida. Intenta de nuevo.")


def pedir_numero(mensaje, minimo=1, maximo=99):
    """Pide un número entero dentro de un rango (Unidad 1: tipos de datos)."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"  ⚠️  Ingresa un número entre {minimo} y {maximo}.")
        except ValueError:
            print("  ⚠️  Debe ser un número entero.")


# ─────────────────────────────────────────────
#  UNIDAD 3 · LÓGICA DE LA COMPUTADORA
# ─────────────────────────────────────────────
def jugada_computadora(dificultad, ultima_jugada_usuario=None):
    """
    Genera la jugada de la computadora según la dificultad.
    - Fácil:  completamente aleatoria
    - Normal: aleatoria con ligera tendencia a ganar
    - Difícil: intenta predecir la jugada del usuario
    """
    if dificultad == "1":   # Fácil
        return random.choice(list(OPCIONES.values()))

    elif dificultad == "2": # Normal — 50% aleatoria, 50% contragolpe
        if random.random() < 0.5 or ultima_jugada_usuario is None:
            return random.choice(list(OPCIONES.values()))
        # Elige la jugada que vence a la última del usuario
        return _jugada_ganadora_contra(ultima_jugada_usuario)

    else:                   # Difícil — intenta contrarrestar siempre
        if ultima_jugada_usuario is None:
            return random.choice(list(OPCIONES.values()))
        return _jugada_ganadora_contra(ultima_jugada_usuario)


def _jugada_ganadora_contra(jugada):
    """Devuelve la jugada que vence a la indicada."""
    tabla = {"Piedra": "Papel", "Papel": "Tijera", "Tijera": "Piedra"}
    return tabla[jugada]


# ─────────────────────────────────────────────
#  UNIDAD 2 · CONDICIONALES — RESULTADO
# ─────────────────────────────────────────────
def determinar_ganador(jugador, computadora):
    """Determina el resultado de la ronda con condicionales."""
    if jugador == computadora:
        return "empate"
    if (jugador, computadora) in COMBINA_GANADORAS:
        return "jugador"
    return "computadora"


# ─────────────────────────────────────────────
#  MARCADOR Y ESTADÍSTICAS
# ─────────────────────────────────────────────
def estadisticas_iniciales():
    """Crea el diccionario de estadísticas vacío."""
    return {
        "rondas": 0, "jugador": 0,
        "computadora": 0, "empates": 0,
        "racha_actual": 0, "mejor_racha": 0
    }


def actualizar_estadisticas(stats, resultado):
    """Actualiza el marcador según el resultado de la ronda (Unidad 3: bucles)."""
    stats["rondas"] += 1
    if resultado == "jugador":
        stats["jugador"] += 1
        stats["racha_actual"] += 1
        if stats["racha_actual"] > stats["mejor_racha"]:
            stats["mejor_racha"] = stats["racha_actual"]
    elif resultado == "computadora":
        stats["computadora"] += 1
        stats["racha_actual"] = 0
    else:
        stats["empates"] += 1
        stats["racha_actual"] = 0


def mostrar_marcador(stats):
    """Muestra las estadísticas en pantalla."""
    titulo("MARCADOR ACTUAL")
    print(f"  Rondas jugadas  : {stats['rondas']}")
    print(f"  Victorias tuyas : {stats['jugador']}")
    print(f"  Victorias CPU   : {stats['computadora']}")
    print(f"  Empates         : {stats['empates']}")
    if stats["rondas"] > 0:
        pct = round(stats["jugador"] / stats["rondas"] * 100, 1)
        print(f"  Tasa de victoria: {pct}%")
    print(f"  Mejor racha     : {stats['mejor_racha']} victorias seguidas")
    separador()


# ─────────────────────────────────────────────
#  PERSISTENCIA — HISTORIAL EN ARCHIVO
# ─────────────────────────────────────────────
def guardar_historial(nombre_jugador, stats, modo):
    """Guarda el resumen de la sesión en un archivo de texto."""
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    linea = (
        f"{fecha} | {nombre_jugador} | Modo: {modo} | "
        f"Rondas: {stats['rondas']} | "
        f"Victorias: {stats['jugador']} | "
        f"CPU: {stats['computadora']} | "
        f"Empates: {stats['empates']}\n"
    )
    try:
        with open(ARCHIVO_HISTORIAL, "a", encoding="utf-8") as f:
            f.write(linea)
        print(f"\n  ✅ Sesión guardada en '{ARCHIVO_HISTORIAL}'.")
    except IOError:
        print("\n  ⚠️  No se pudo guardar el historial.")


def ver_historial():
    """Lee y muestra el historial de partidas guardadas."""
    titulo("HISTORIAL DE PARTIDAS")
    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        if not lineas:
            print("  No hay partidas registradas aún.")
        else:
            for i, linea in enumerate(lineas[-10:], 1):   # Últimas 10
                print(f"  {i}. {linea.strip()}")
    except FileNotFoundError:
        print("  No hay historial guardado todavía.")
    separador()


# ─────────────────────────────────────────────
#  UNIDAD 3 · BUCLE DE JUEGO — RONDA SIMPLE
# ─────────────────────────────────────────────
def jugar_ronda(stats, dificultad, ultima_jugada):
    """Ejecuta una ronda completa y devuelve la jugada del usuario."""
    jugador    = pedir_jugada()
    computadora = jugada_computadora(dificultad, ultima_jugada)

    print(f"\n  Tú elegiste  : {EMOJIS[jugador]}  {jugador}")
    print(f"  CPU eligió   : {EMOJIS[computadora]}  {computadora}")

    resultado = determinar_ganador(jugador, computadora)
    actualizar_estadisticas(stats, resultado)

    if resultado == "jugador":
        print("  🎉  ¡Ganaste esta ronda!")
    elif resultado == "computadora":
        print("  😞  La computadora ganó esta ronda.")
    else:
        print("  🤝  ¡Empate!")

    return jugador   # Se guarda para la dificultad


# ─────────────────────────────────────────────
#  MODO TORNEO (al mejor de N rondas)
# ─────────────────────────────────────────────
def modo_torneo(nombre_jugador, dificultad):
    """Juega un torneo al mejor de N rondas."""
    titulo(f"TORNEO — {nombre_jugador}")
    rondas_ganar = pedir_numero(
        "  ¿Cuántas victorias para ganar el torneo? (1-10): ", 1, 10
    )
    stats = estadisticas_iniciales()
    ultima_jugada = None

    # Unidad 3: bucle while con condición múltiple
    while stats["jugador"] < rondas_ganar and stats["computadora"] < rondas_ganar:
        print(f"\n  🏆  Marcador → Tú: {stats['jugador']}  |  CPU: {stats['computadora']}"
              f"  (Gana quien llegue a {rondas_ganar})")
        separador("-", 42)
        ultima_jugada = jugar_ronda(stats, dificultad, ultima_jugada)

    titulo("RESULTADO DEL TORNEO")
    if stats["jugador"] >= rondas_ganar:
        print(f"  🏆  ¡Felicitaciones {nombre_jugador}! Ganaste el torneo.")
    else:
        print("  🤖  La computadora ganó el torneo. ¡Sigue intentando!")

    mostrar_marcador(stats)
    guardar_historial(nombre_jugador, stats, "Torneo")


# ─────────────────────────────────────────────
#  MODO LIBRE (rondas ilimitadas)
# ─────────────────────────────────────────────
def modo_libre(nombre_jugador, dificultad):
    """Juega rondas libres hasta que el usuario decida salir."""
    stats = estadisticas_iniciales()
    ultima_jugada = None

    while True:
        titulo(f"RONDA {stats['rondas'] + 1} — {nombre_jugador}")
        ultima_jugada = jugar_ronda(stats, dificultad, ultima_jugada)

        print("\n  ¿Qué deseas hacer?")
        print("  1. Jugar otra ronda")
        print("  2. Ver marcador")
        print("  3. Salir al menú principal")
        opcion = input("  → ").strip()

        if opcion == "2":
            mostrar_marcador(stats)
        elif opcion == "3":
            mostrar_marcador(stats)
            guardar_historial(nombre_jugador, stats, "Libre")
            break
        elif opcion != "1":
            print("  ⚠️  Opción no válida, se continúa el juego.")


# ─────────────────────────────────────────────
#  CONFIGURACIÓN DE DIFICULTAD
# ─────────────────────────────────────────────
def seleccionar_dificultad():
    """Permite elegir la dificultad de la computadora."""
    titulo("SELECCIONA DIFICULTAD")
    print("  1. 😊  Fácil  — CPU completamente aleatoria")
    print("  2. 😐  Normal — CPU con algo de estrategia")
    print("  3. 😈  Difícil— CPU intenta predecirte")
    while True:
        opcion = input("  → Elige 1, 2 o 3: ").strip()
        if opcion in ("1", "2", "3"):
            nombres = {"1": "Fácil", "2": "Normal", "3": "Difícil"}
            print(f"\n  ✅ Dificultad seleccionada: {nombres[opcion]}")
            return opcion
        print("  ⚠️  Opción inválida.")


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────
def menu_principal():
    """Controla el flujo general del programa (Unidad 3: bucle principal)."""
    titulo("PIEDRA, PAPEL O TIJERA — EDICIÓN AVANZADA")
    print("  Bienvenido al Proyecto Integrador")
    print("  Lógica de Programación · UIDE 2026")
    separador()

    nombre_jugador = input("  ¿Cuál es tu nombre? ").strip() or "Jugador"
    print(f"\n  ¡Hola, {nombre_jugador}! 👋")

    dificultad = seleccionar_dificultad()

    # Unidad 3: bucle principal del menú
    while True:
        titulo(f"MENÚ PRINCIPAL — {nombre_jugador}")
        print("  1. 🎮  Jugar en modo libre")
        print("  2. 🏆  Jugar en modo torneo")
        print("  3. 📋  Ver reglas")
        print("  4. 📊  Ver historial de partidas")
        print("  5. ⚙️  Cambiar dificultad")
        print("  6. 🚪  Salir")
        separador("-", 42)

        opcion = input("  → Selecciona una opción: ").strip()

        if opcion == "1":
            modo_libre(nombre_jugador, dificultad)
        elif opcion == "2":
            modo_torneo(nombre_jugador, dificultad)
        elif opcion == "3":
            mostrar_reglas()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            dificultad = seleccionar_dificultad()
        elif opcion == "6":
            titulo("¡HASTA LUEGO!")
            print(f"  Gracias por jugar, {nombre_jugador}. 👋")
            separador()
            break
        else:
            print("  ⚠️   Opción no válida. Intenta de nuevo.")


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    menu_principal()
