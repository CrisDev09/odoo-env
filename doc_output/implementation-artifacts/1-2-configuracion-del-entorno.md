# Story 1.2: Configuración del Entorno

Status: review

<!-- Note: Validation is optional. Run validate-create-story for quality check before dev-story. -->

## Story

Como un Desarrollador,
quiero configurar la versión de Odoo, las credenciales de la base de datos y los nombres de los contenedores usando un archivo de entorno,
para que pueda adaptar el entorno y evitar conflictos con otros proyectos.

## Acceptance Criteria

1.  **Dado que** tengo un entorno ejecutándose desde la Historia 1.1,
2.  **Y** tengo un archivo `.env` con las variables `ODOO_VERSION`, `POSTGRES_PASSWORD` y una variable para el nombre del proyecto (ej. `PROJECT_NAME`),
3.  **Cuando** reconstruyo y lanzo el contenedor a través de "Reopen in Container",
4.  **Entonces** la instancia de Odoo utiliza la versión especificada.
5.  **Y** el contenedor de Odoo se conecta a la base de datos utilizando las credenciales especificadas.
6.  **Y** los contenedores de Docker creados se nombran usando la variable `PROJECT_NAME` para asegurar su unicidad (ej. `mi-proyecto_odoo_1`, `mi-proyecto_db_1`).

## Tasks / Subtasks

- [x] **Tarea 1: Modificar `docker-compose.yml` para usar variables de entorno.**
    - [x] Actualizar el servicio `odoo` para leer `ODOO_VERSION` del entorno.
    - [x] Actualizar el servicio `db` para leer `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` del entorno.
    - [x] Actualizar el servicio `odoo` para usar las variables de entorno de la DB para la conexión.
    - [x] Modificar los nombres de los servicios para que incluyan `PROJECT_NAME` (ej. `$\{PROJECT_NAME\}_odoo_1`).

- [x] **Tarea 2: Crear un archivo `.env.example` en `.devcontainer/.`**
    - [x] Incluir variables `ODOO_VERSION`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `PROJECT_NAME`, `OE_SUPERADMIN_PASS`.
    - [x] Proporcionar valores por defecto razonables (ej. `ODOO_VERSION=17.0`, `POSTGRES_DB=odoo_db`, etc.).

- [x] **Tarea 3: Actualizar `devcontainer.json` para cargar el archivo `.env`.**
    - [x] Añadir la configuración para cargar el archivo `.env` en el contenedor.

- [x] **Tarea 4: Asegurar que `.env` esté en `.gitignore`.** (Ya se hizo en Story 1.1, pero se verifica).

## Dev Notes

- **Paso clave:** La configuración de las variables de entorno se realizará en el `docker-compose.yml`. Las credenciales de la base de datos y la versión de Odoo serán dinámicas.
- **Gestión de Secretos:** Utilizar un archivo `.env` (no versionado) es la mejor práctica para manejar credenciales sensibles.
- **Nomenclatura de Contenedores:** La variable `PROJECT_NAME` se utilizará para prefijar los nombres de los servicios de Docker Compose, asegurando unicidad en entornos con múltiples proyectos.
- **Versiones Recomendadas:** Por arquitectura, se recomienda Odoo 17, Python 3.10 y PostgreSQL 12. La configurable `ODOO_VERSION` debe respetar estas directrices.
- **Referencia:** Web research confirma las variables de entorno estándar para Odoo y PostgreSQL en Docker Compose.

### Project Structure Notes

- **Archivo `.env.example`:** Se creará en el directorio `.devcontainer/` como plantilla para los desarrolladores.
- **Modificaciones:** Se modificarán los archivos `docker-compose.yml` y `devcontainer.json` dentro de `.devcontainer/`.
- **No impacto en la estructura de addons:** Esta historia no afectará directamente la estructura de módulos de Odoo, sino la configuración del entorno que los aloja.

### References

*   [Source: doc_output/planning-artifacts/architecture.md#Pila Tecnológica Seleccionada]
*   [Source: doc_output/planning-artifacts/architecture.md#Estrategia de Gestión de Configuración Extendida]
*   [Source: doc_output/planning-artifacts/epics.md#Story 1.2: Configuración del Entorno]
*   [Source: Web search results for Odoo 17, PostgreSQL 12, Python 3.10 environment variables in Docker Compose]

## Dev Agent Record

### Agent Model Used

Gemini CLI Agent

### Debug Log References

### Completion Notes List
- Implementadas las modificaciones en `docker-compose.yml` para usar variables de entorno `ODOO_VERSION`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, y `PROJECT_NAME` para los nombres de los contenedores.
- Creado el archivo `.devcontainer/.env.example` con valores por defecto.
- Añadido `initializeCommand` en `devcontainer.json` para copiar `.env.example` a `.env` si no existe.
- Verificado que `.env` está en `.gitignore`.

### File List
- `.devcontainer/docker-compose.yml` (modificado)
- `.devcontainer/.env.example` (nuevo)
- `.devcontainer/devcontainer.json` (modificado)
- `.gitignore` (modificado)
