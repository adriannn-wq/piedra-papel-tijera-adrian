# Guion para el video explicativo

**Duración sugerida:** 2 a 3 minutos.

## 1. Presentación (10–15 segundos)
> Buenos días. Mi nombre es Adrian Alejandro Ron Albarracin y presento el avance inicial de mi proyecto de Lógica de Programación. El programa seleccionado es un juego de Piedra, Papel o Tijera desarrollado en Python.

## 2. Configuración del repositorio (20–30 segundos)
> En GitHub creé el repositorio llamado “piedra-papel-tijera-adrian”. Dentro del repositorio organicé el proyecto en carpetas: `src` contiene el código, `diagramas` contiene los diagramas de flujo y `docs` incluye la guía y el guion del video. También agregué un archivo README con la descripción y los pasos de ejecución.

**Mientras hablas:** abre la página principal del repositorio y muestra las carpetas.

## 3. Explicación de los diagramas (30–40 segundos)
> El diagrama principal representa el proceso general del juego: el usuario elige una opción, la computadora genera una jugada aleatoria, se comparan las elecciones y se pregunta si se desea continuar. El diagrama de validación evita que el usuario ingrese datos diferentes de 1, 2 o 3. Finalmente, el diagrama de resultado representa las condiciones que determinan si gana el jugador, la computadora o si hay empate.

**Mientras hablas:** abre los tres diagramas.

## 4. Avance del código (40–60 segundos)
> El código se desarrolló en Python usando Visual Studio Code. En esta versión ya se implementaron las reglas del juego, la validación de la entrada, la elección aleatoria de la computadora, la comparación de resultados y un marcador acumulado. La función `pedir_jugada` corresponde al diagrama de validación, la función `determinar_ganador` corresponde al diagrama de resultado y la función `jugar` coordina el flujo principal.

**Mientras hablas:** muestra `src/main.py` y señala las funciones mencionadas.

## 5. Demostración (30–40 segundos)
> Al ejecutar el programa, el usuario puede seleccionar Piedra, Papel o Tijera. El sistema muestra la opción de la computadora, indica el ganador y actualiza el marcador. Después pregunta si se desea jugar otra ronda, lo que permite repetir el ciclo hasta finalizar el juego.

**Mientras hablas:** corre `python src/main.py` y juega una ronda.

## 6. Cierre (10 segundos)
> Con este avance se evidencia la relación entre los diagramas de flujo y la codificación del programa. En una siguiente fase se podrían agregar niveles de dificultad, historial de partidas y una interfaz gráfica. Gracias.
