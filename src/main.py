
"""
Proyecto: Piedra, Papel o Tijera
Autor: Adrian Alejandro Ron Albarracin
Materia: Lógica de Programación

Paso 2:
- Menú principal.
- Condicionales.
- Bucles.
- Marcador y estadísticas.
"""

import random

# Opciones disponibles para el jugador
OPCIONES = {
    "1": "Piedra",
    "2": "Papel",
    "3": "Tijera"
}


def mostrar_reglas():
    """Muestra las reglas principales del juego."""
    print("\n--- REGLAS DEL JUEGO ---")
    print("Piedra gana a Tijera.")
    print("Tijera gana a Papel.")
    print("Papel gana a Piedra.")


def pedir_jugada():
    """Solicita y valida la jugada del usuario."""
    while True:
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        opcion = input("Escribe 1, 2 o 3: ").strip()

        if opcion in OPCIONES:
            return OPCIONES[opcion]

        print("Entrada no válida. Intenta nuevamente.")


def jugada_computadora():
    """Genera una elección aleatoria para la computadora."""
    return random.choice(list(OPCIONES.values()))


def determinar_ganador(jugador, computadora):
    """Compara ambas jugadas y devuelve el resultado."""
    if jugador == computadora:
        return "empate"

    combinaciones_ganadoras = {
        ("Piedra", "Tijera"),
        ("Papel", "Piedra"),
        ("Tijera", "Papel")
    }

    if (jugador, computadora) in combinaciones_ganadoras:
        return "jugador"

    return "computadora"


def mostrar_marcador(estadisticas):
    """Muestra las estadísticas acumuladas."""
    print("\n--- MARCADOR ---")
    print("Rondas jugadas:", estadisticas["rondas"])
    print("Victorias del jugador:", estadisticas["jugador"])
    print("Victorias de la computadora:", estadisticas["computadora"])
    print("Empates:", estadisticas["empates"])


def jugar_ronda(estadisticas):
    """Ejecuta una ronda completa del juego."""
    jugador = pedir_jugada()
    computadora = jugada_computadora()

    print("\nTu elección fue:", jugador)
    print("La computadora eligió:", computadora)

    resultado = determinar_ganador(jugador, computadora)

    # Se actualiza el marcador según el resultado
    estadisticas["rondas"] += 1

    if resultado == "jugador":
        estadisticas["jugador"] += 1
        print("Resultado: ¡Ganaste esta ronda!")
    elif resultado == "computadora":
        estadisticas["computadora"] += 1
        print("Resultado: La computadora ganó esta ronda.")
    else:
        estadisticas["empates"] += 1
        print("Resultado: Empate.")


def menu_principal():
    """Controla el menú principal del programa."""
    estadisticas = {
        "rondas": 0,
        "jugador": 0,
        "computadora": 0,
        "empates": 0
    }

    while True:
        print("\n==============================")
        print("   PIEDRA, PAPEL O TIJERA")
        print("==============================")
        print("1. Jugar una ronda")
        print("2. Ver reglas")
        print("3. Ver marcador")
        print("4. Salir")

        opcion_menu = input("Selecciona una opción: ").strip()

        if opcion_menu == "1":
            jugar_ronda(estadisticas)
        elif opcion_menu == "2":
            mostrar_reglas()
        elif opcion_menu == "3":
            mostrar_marcador(estadisticas)
        elif opcion_menu == "4":
            print("\nGracias por jugar.")
            mostrar_marcador(estadisticas)
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu_principal()
```
