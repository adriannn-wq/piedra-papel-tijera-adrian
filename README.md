#  Piedra, Papel o Tijera — Edición Terminada

**Proyecto Integrador · Lógica de Programación · UIDE **

---

##  Nombre del proyecto

**El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas**  
*Implementación práctica: Sistema de juego interactivo Piedra, Papel o Tijera — Edición Avanzada*

---

##  Integrantes

| Nombre | Universidad |
|--------|-------------|
| Adrian Alejandro Ron Albarracín | Universidad Internacional del Ecuador (UIDE) |

**Docente:** Lilian Marlene Aman Ramos  
**Asignatura:** Lógica de Programación  
**Fecha:** Quito, junio 2026

---

##  Objetivo del sistema

Desarrollar una aplicación de consola en Python que extienda el juego clásico de Piedra, Papel o Tijera, integrando los conceptos de las cuatro unidades de la asignatura: variables y tipos de datos, estructuras condicionales, estructuras repetitivas, y organización modular del código mediante funciones.

---

##  Descripción de funcionalidades

### Funcionalidades nuevas (extensión del proyecto original)

| Funcionalidad | Descripción |
|---|---|
| **Modo libre** | Juega rondas ilimitadas hasta decidir salir |
| **Modo torneo** | Juega al mejor de N victorias definidas por el jugador |
| **Niveles de dificultad** | Fácil (aleatoria), Normal (semi-estratégica), Difícil (predictiva) |
| **Estadísticas avanzadas** | Tasa de victoria, racha actual y mejor racha |
| **Historial persistente** | Guarda el resumen de cada sesión en un archivo `.txt` |
| **Nombre del jugador** | El sistema saluda y personaliza la experiencia |
| **Interfaz mejorada** | Emojis, separadores visuales y menú estructurado |

### Funcionalidades heredadas del proyecto anterior

- Validación de entrada del usuario
- Selección aleatoria de la computadora
- Determinación del ganador por condicionales
- Marcador de victorias y empates
- Repetición de rondas mediante bucles

---

##  Estructura del repositorio

```
piedra-papel-tijera-adrian/
├── src/
│   ├── main.py              ← Versión original (Actividad Autónoma 1)
│   └── main_avanzado.py     ← Versión extendida (Proyecto Integrador)
├── diagramas/
│   ├── diagrama_casos_uso.png
│   ├── diagrama_arquitectura.png
│   ├── diagrama_principal.png
│   ├── diagrama_validacion.png
│   └── diagrama_resultado.png
├── docs/
│   └── documento_proyecto.docx
├── README.md
└── historial_partidas.txt   ← Generado automáticamente al jugar
```

---

##  Relación con las unidades de la asignatura

| Unidad | Tema | Aplicación en el proyecto |
|--------|------|--------------------------|
| **1** | Fundamentos y tipos de datos | Variables, constantes, entrada de texto y números |
| **2** | Condicionales | Validación de jugadas, determinación del ganador |
| **3** | Estructuras repetitivas | Menú principal, bucle de rondas, bucle de torneo |
| **4** | Funciones y organización | Código modularizado en funciones con responsabilidad única |

---

## Tecnologías y entorno

- **Lenguaje:** Python 3.x
- **IDE recomendado:** Visual Studio Code
- **Control de versiones:** Git y GitHub
- **Dependencias externas:** Ninguna (solo biblioteca estándar de Python)

---

##  Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/adriannn-wq/piedra-papel-tijera-adrian.git
cd piedra-papel-tijera-adrian

# Ejecutar la versión extendida
python src/main_avanzado.py

# Ejecutar la versión original
python src/main.py
```

---

## Impacto tecnológico

Este proyecto refleja cómo las tecnologías de software permiten transformar un juego analógico en una experiencia digital interactiva con lógica de inteligencia artificial básica (niveles de dificultad), persistencia de datos y retroalimentación inmediata al usuario. Demuestra que incluso aplicaciones sencillas integran principios fundamentales de programación presentes en sistemas mucho más complejos.
