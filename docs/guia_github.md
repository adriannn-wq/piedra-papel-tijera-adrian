# Guía para crear y subir el repositorio en GitHub

## Opción recomendada: desde la página de GitHub
1. Ingresa a GitHub e inicia sesión.
2. Pulsa **New repository**.
3. Usa el nombre: `piedra-papel-tijera-adrian`.
4. Selecciona **Public** si la docente debe acceder sin permisos. Si la consigna indica privado, selecciona **Private** e invita a la docente.
5. No marques la opción para crear README, porque este proyecto ya incluye uno.
6. Presiona **Create repository**.
7. Selecciona **Add file > Upload files**.
8. Arrastra todos los archivos y carpetas de este proyecto.
9. Escribe como primer commit: `Crear estructura inicial y avance del juego`.
10. Copia el enlace del repositorio y entrégalo en la plataforma.

## Opción con terminal (Git)
Abre la terminal en la carpeta del proyecto y ejecuta:

```bash
git init
git add .
git commit -m "Crear estructura inicial y avance del juego"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/piedra-papel-tijera-adrian.git
git push -u origin main
```

## Commits sugeridos para una mejor evidencia
1. `Crear estructura inicial del proyecto`
2. `Agregar diagramas de flujo del juego`
3. `Implementar lógica inicial de Piedra Papel o Tijera`
4. `Actualizar documentación y guía de ejecución`

## Qué debe verse en el repositorio
- El código dentro de `src/main.py`.
- Los tres diagramas en la carpeta `diagramas`.
- El archivo `README.md` abierto en la página principal.
- Los commits realizados.
