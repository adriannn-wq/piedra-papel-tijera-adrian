"""
Proyecto: Piedra, Papel o Tijera
Autor: Adrian Alejandro Ron Albarracin
Materia: Lógica de Programación

Avance inicial funcional:
- Menú principal.
- Validación de la opción del usuario.
- Selección aleatoria de la computadora.
- Comparación de jugadas.
- Marcador durante la sesión.
- Opción para repetir partidas.
"""

import random

OPCIONES = {
    "1": "Piedra",
    "2": "Papel",
    "3": "Tijera",
}


def mostrar_reglas() -> None:
    """Muestra al usuario las reglas básicas del juego."""
    print("\nREGLAS DEL JUEGO")
    print("- Piedra gana a Tijera.")
    print("- Tijera gana a Papel.")
    print("- Papel gana a Piedra.\n")


def pedir_jugada() -> str:
    """Solicita una jugada válida y devuelve Piedra, Papel o Tijera."""
    while True:
        print("Elige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        opcion = input("Escribe 1, 2 o 3: ").strip()

        if opcion in OPCIONES:
            return OPCIONES[opcion]

        print("\nEntrada no válida. Intenta nuevamente.\n")


def jugada_computadora() -> str:
    """Genera una jugada aleatoria para la computadora."""
    return random.choice(list(OPCIONES.values()))


def determinar_ganador(jugador: str, computadora: str) -> str:
    """Compara ambas jugadas y devuelve el resultado de la ronda."""
    if jugador == computadora:
        return "empate"

    combinaciones_ganadoras = {
        ("Piedra", "Tijera"),
        ("Papel", "Piedra"),
        ("Tijera", "Papel"),
    }

    if (jugador, computadora) in combinaciones_ganadoras:
        return "jugador"

    return "computadora"


def preguntar_revancha() -> bool:
    """Pregunta si se desea continuar jugando."""
    while True:
        respuesta = input("¿Deseas jugar otra ronda? (s/n): ").strip().lower()
        if respuesta in {"s", "si", "sí"}:
            return True
        if respuesta in {"n", "no"}:
            return False
        print("Respuesta no válida. Escribe s o n.")


def jugar() -> None:
    """Controla el flujo principal del juego y el marcador."""
    victorias_jugador = 0
    victorias_computadora = 0
    empates = 0

    print("=" * 42)
    print("      PIEDRA, PAPEL O TIJERA")
    print("=" * 42)
    mostrar_reglas()

    continuar = True
    while continuar:
        jugador = pedir_jugada()
        computadora = jugada_computadora()
        resultado = determinar_ganador(jugador, computadora)

        print(f"\nTu elección: {jugador}")
        print(f"Elección de la computadora: {computadora}")

        if resultado == "jugador":
            victorias_jugador += 1
            print("Resultado: ¡Ganaste esta ronda!")
        elif resultado == "computadora":
            victorias_computadora += 1
            print("Resultado: La computadora ganó esta ronda.")
        else:
            empates += 1
            print("Resultado: Empate.")

        print("\nMARCADOR ACTUAL")
        print(f"Jugador: {victorias_jugador}")
        print(f"Computadora: {victorias_computadora}")
        print(f"Empates: {empates}\n")

        continuar = preguntar_revancha()

    print("\nGracias por jugar.")
    print("MARCADOR FINAL")
    print(f"Jugador: {victorias_jugador}")
    print(f"Computadora: {victorias_computadora}")
    print(f"Empates: {empates}")


if __name__ == "__main__":
    jugar()
