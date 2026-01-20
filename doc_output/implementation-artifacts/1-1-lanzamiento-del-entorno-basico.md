# Story 1.1: Lanzamiento del Entorno Básico

**Estado:** `review`
**Épica:** [Épica 1: Entorno de Desarrollo Fundamental](file://C:\Users\cacde\projects\cristian\odoo-env\doc_output\planning-artifacts\epics.md)
**Documento de Arquitectura:** [Architecture Decision Document](file://C:\Users\cacde\projects\cristian\odoo-env\doc_output\planning-artifacts\architecture.md)
**PRD:** [Product Requirements Document (PRD) - odoo-env](file://C:\Users\cacde\projects\cristian\odoo-env\doc_output\planning-artifacts\prd.md)

## 1. Requisitos de la Historia

### User Story

Como un Desarrollador,
quiero lanzar los servicios de Odoo y la base de datos usando un solo comando,
para que pueda tener un entorno base funcional.

### Criterios de Aceptación

1.  **Dado que** tengo Docker y VS Code instalados, **cuando** ejecuto el comando "Reopen in Container" desde VS Code, **entonces** se crean y se inician sin errores un contenedor de Odoo y un contenedor de PostgreSQL.
2.  **Y** los registros (logs) del contenedor de Odoo indican que el servidor se ha iniciado correctamente y está listo para aceptar conexiones.

## 2. Contexto para el Desarrollador (Developer Context)

Esta historia es la base de todo el proyecto. El objetivo es crear la estructura de directorios y los archivos de configuración esenciales que permitan a VS Code y Docker orquestar un entorno de desarrollo de Odoo funcional y reproducible.

### Requisitos Técnicos y Arquitectónicos

*   **Pila Tecnológica Principal:**
    *   **Odoo:** Versión 17
    *   **Python:** Versión 3.10
    *   **PostgreSQL:** Versión 12
    *   **Referencia:** `doc_output/planning-artifacts/architecture.md` > "Pila Tecnológica Seleccionada"

*   **Contenerización:**
    *   La solución DEBE usar **Docker** con **Docker Compose** para definir y ejecutar el entorno multi-contenedor.
    *   La integración con el IDE DEBE ser a través de **VS Code Dev Containers**.
    *   **Referencia:** `doc_output/planning-artifacts/architecture.md` > "Contenerización y Orquestación"

*   **Seguridad y Permisos:**
    *   Se DEBE crear un **usuario (`odoo`) y grupo (`odoo`) sin privilegios de root** dentro del contenedor de Odoo.
    *   Este usuario poseerá los archivos de la aplicación y ejecutará el proceso de Odoo.
    *   **Referencia:** `doc_output/planning-artifacts/architecture.md` > "Entorno de Desarrollo y Herramientas"

*   **Entorno de Shell:**
    *   El shell por defecto para el usuario `odoo` DEBE ser **Zsh**.
    *   Se DEBE instalar **Oh My Zsh** junto con los plugins `zsh-autosuggestions` y `zsh-syntax-highlighting`.
    *   **Referencia:** `doc_output/planning-artifacts/architecture.md` > "Entorno de Desarrollo y Herramientas"

### Estructura de Archivos a Implementar

La implementación de esta historia requiere la creación de la siguiente estructura de archivos y directorios. Presta mucha atención a las rutas.

```
odoo-env/
├── .devcontainer/                         # Directorio principal para la configuración
│   ├── devcontainer.json                  # DEFINE la configuración del Dev Container (extensiones, puertos, etc.)
│   ├── docker-compose.yml                 # DEFINE los servicios de Docker (odoo, db)
│   └── build/                             # Directorio para los artefactos de construcción de la imagen
│       ├── Dockerfile                     # DEFINE la imagen de Odoo (instala Python, Zsh, crea usuario)
│       ├── entrypoint.sh                  # Script de entrada para el contenedor de Odoo
│       └── wait-for-psql.py               # Script de utilidad para esperar a que PostgreSQL esté listo
├── .gitignore                             # DEBE contener .env para evitar subir secretos
└── .vscode/
    └── launch.json                        # Contendrá las configuraciones de depuración en historias futuras
```
**Referencia:** `doc_output/planning-artifacts/architecture.md` > "Complete Project Directory Structure"

### Requisitos de Pruebas

*   La validación para esta historia es principalmente manual, verificando que los contenedores se inicien correctamente y que el entorno sea accesible.
*   No se requieren pruebas automatizadas para esta historia inicial.

## 3. Tareas de Implementación

- [x] **Tarea 1: Crear la estructura de directorios base.**
    - Crear el directorio `.devcontainer/` y su subdirectorio `build/`.
    - Crear el directorio `.vscode/`.

- [x] **Tarea 2: Implementar el `Dockerfile`.** (AC: 1)
    - Usar la imagen base de Python 3.10.
    - Instalar dependencias del sistema necesarias para Odoo y PostgreSQL client.
    - Instalar Zsh, Oh My Zsh y los plugins.
    - Crear el usuario y grupo `odoo`.
    - Configurar los permisos y el directorio de trabajo.
    - Copiar los scripts `entrypoint.sh` y `wait-for-psql.py`.

- [x] **Tarea 3: Implementar los scripts de soporte (`entrypoint.sh`, `wait-for-psql.py`).** (AC: 1, 2)
    - `wait-for-psql.py`: Escribir un script de Python que intente conectarse a la base de datos en un bucle hasta que tenga éxito.
    - `entrypoint.sh`: Escribir un script de shell que primero ejecute `wait-for-psql.py` y luego inicie el proceso de Odoo.

- [x] **Tarea 4: Implementar `docker-compose.yml`.** (AC: 1)
    - Definir el servicio `odoo` que se construye a partir del `Dockerfile`.
    - Definir el servicio `db` usando la imagen oficial de `postgres:12`.
    - Configurar la red y los volúmenes necesarios.
    - Usar variables de entorno para la configuración de la base de datos (se definirá en la historia 1.2).

- [x] **Tarea 5: Implementar `devcontainer.json`.** (AC: 1)
    - Configurar el archivo para que use el `docker-compose.yml`.
    - Especificar el servicio `odoo` como el servicio principal.
    - Definir el `workspaceFolder` y el `remoteUser`.
    - Dejar una sección de `extensions` vacía por ahora (se llenará en la historia 1.4).

- [x] **Tarea 6: Crear y configurar `.gitignore`.**
    - Añadir `.env` al archivo `.gitignore`.

## 4. Notas Finales de la Historia

- **Estado de Finalización:** `ready-for-dev`
- **Notas:** El análisis del motor de contexto definitivo ha concluido. Esta guía proporciona al desarrollador todo lo necesario para una implementación impecable de la Historia 1.1.

---
## 5. File List
- `.devcontainer/` (directorio)
- `.devcontainer/build/` (directorio)
- `.vscode/` (directorio)
- `.devcontainer/build/Dockerfile`
- `.devcontainer/build/wait-for-psql.py`
- `.devcontainer/build/entrypoint.sh`
- `.devcontainer/docker-compose.yml`
- `.devcontainer/devcontainer.json`
- `.gitignore` (modificado)

## 6. Dev Agent Record

### Completion Notes
- **Tarea 1:** Se ha creado la estructura de directorios base (`.devcontainer/build/`, `.vscode/`) utilizando el comando `New-Item`. Se verificó que los directorios existen.
- **Tarea 2:** Se ha creado el archivo `.devcontainer/build/Dockerfile`. Este archivo define la imagen de Docker para el servicio de Odoo, incluyendo la instalación de dependencias del sistema, la creación de un usuario `odoo` no privilegiado y la configuración de Zsh con Oh My Zsh.
- **Tarea 3:** Se han creado los scripts de soporte. `wait-for-psql.py` asegura que el servicio de base de datos esté disponible antes de iniciar Odoo. `entrypoint.sh` orquesta el inicio, ejecutando primero el script de espera y luego el proceso de Odoo.
- **Tarea 4:** Se ha creado el archivo `.devcontainer/docker-compose.yml`. Define los servicios `odoo` y `db`, sus dependencias, volúmenes y puertos. Utiliza placeholders para las variables de entorno de la base de datos, que se gestionarán en una historia posterior.
- **Tarea 5:** Se ha creado el archivo `.devcontainer/devcontainer.json`. Este archivo configura la integración con VS Code Dev Containers, especificando el `docker-compose.yml` a utilizar, el servicio principal (`odoo`), el directorio de trabajo y el usuario remoto.
- **Tarea 6:** Se ha añadido la entrada `.env` al archivo `.gitignore` para asegurar que los archivos de entorno locales no se incluyan en el control de versiones.

## 7. Change Log
- **2026-01-19:** Implementada la estructura completa del Dev Container para el lanzamiento básico del entorno Odoo. Creados Dockerfile, scripts de soporte, docker-compose.yml y devcontainer.json.
