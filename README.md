# Piedra, Papel o Tijera

**Autor:** Adrian Alejandro Ron Albarracin  
**Materia:** Lógica de Programación  
**Tipo de proyecto:** Aplicación de consola en Python  

## Descripción
Este proyecto corresponde a un avance inicial de un juego de consola llamado **Piedra, Papel o Tijera**. El programa permite que una persona juegue contra la computadora, valida la opción ingresada, genera una elección aleatoria y muestra el resultado de cada ronda junto con un marcador acumulado.

## Funcionalidades implementadas
- Presentación de las reglas del juego.
- Selección de Piedra, Papel o Tijera por parte del usuario.
- Validación de datos ingresados.
- Selección aleatoria de la computadora.
- Comparación de jugadas y determinación del ganador.
- Marcador de victorias del jugador, computadora y empates.
- Repetición de rondas hasta que el usuario decida salir.

## Relación con los diagramas de flujo
- `diagrama_principal`: representa el ciclo completo de una partida, desde el ingreso de la jugada hasta la repetición o finalización.
- `diagrama_validacion`: representa la verificación de que el usuario ingrese una opción permitida.
- `diagrama_resultado`: representa la lógica que decide si gana el jugador, la computadora o si existe empate.

## Tecnologías y entorno
- Lenguaje: Python 3.
- IDE recomendado: Visual Studio Code.
- Control de versiones: Git y GitHub.
- Dependencias externas: ninguna.

## Ejecución
1. Instalar Python 3.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python src/main.py
```

## Estructura del repositorio
```text
piedra-papel-tijera-adrian/
├── src/
│   └── main.py
├── diagramas/
│   ├── diagrama_principal.png
│   ├── diagrama_validacion.png
│   └── diagrama_resultado.png
├── docs/
│   ├── guia_github.md
│   └── guion_video.md
├── README.md
├── .gitignore
└── requirements.txt
```
