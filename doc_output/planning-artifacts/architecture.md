---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7]
inputDocuments: []
workflowType: 'architecture'
project_name: 'odoo-env'
user_name: 'cris'
date: '2026-01-16'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

## Análisis del Contexto del Proyecto

### Visión General de los Requisitos

**Requisitos Funcionales:**
El proyecto abarca un conjunto completo de 19 requisitos funcionales centrados en proporcionar un entorno de desarrollo estandarizado, reproducible y fácil de usar para Odoo. Arquitectónicamente, esto implica la necesidad de estrategias de contenerización robustas (Docker, Dev Containers), una integración perfecta con las características del IDE (`launch.json` de VS Code), una gestión eficiente de las dependencias (`requirements.txt`) y herramientas automatizadas para el ciclo de vida de los módulos de Odoo. El sistema debe soportar varias etapas, desde la inicialización del entorno hasta la depuración, las pruebas y la paridad con producción.

**Requisitos No Funcionales:**
*   **Rendimiento:** La inicialización rápida del entorno (< 2 min después de la construcción) y las interacciones responsivas de Odoo (< 3 seg) requerirán imágenes Docker optimizadas, asignación eficiente de recursos del contenedor y, potencialmente, monitorización del rendimiento dentro del entorno de desarrollo.
*   **Seguridad:** La gestión segura de las credenciales de Git (por ejemplo, reenvío de SSH-Agent) es fundamental y exige una configuración cuidadosa del contexto de seguridad del Dev Container. La gestión de secretos (`.env`, `.gitignore`) también es clave.
*   **Escalabilidad:** El soporte para 10-15 desarrolladores concurrentes apunta a la necesidad de una solución que no consuma muchos recursos en máquinas individuales y que sea fácilmente replicable.
*   **Fiabilidad:** El funcionamiento consistente durante una jornada laboral de 8 horas implica una configuración Docker estable y configuraciones bien probadas.

**Escala y Complejidad:**
El proyecto es un MVP de plataforma, centrado en construir una base técnica sólida y reutilizable para el desarrollo eficiente de Odoo.

- Dominio principal: Entorno de desarrollo full-stack (backend, frontend, infraestructura).
- Nivel de complejidad: Medio.
- Componentes arquitectónicos estimados: 6 (Docker images para Odoo y PostgreSQL, configuraciones de Docker Compose, configuraciones de Dev Container de VS Code, scripts personalizados para automatización y posible configuración de proxy inverso).

### Restricciones y Dependencias Técnicas

*   Dependencia estricta de Docker y VS Code Dev Containers.
*   Dirigido específicamente a Odoo, lo que implica el conocimiento de su arquitectura (Python, PostgreSQL).
*   Compatibilidad multiplataforma (Windows, macOS, Linux).
*   La configuración se basa en archivos `.env` y `requirements.txt`.

### Preocupaciones Transversales Identificadas

*   **Experiencia del Desarrollador (DX):** Es fundamental para el éxito del proyecto e influye en todas las decisiones arquitectónicas.
*   **Coherencia del Entorno (Paridad Dev/Prod):** Impulsa la elección de Docker y la integración CI/CD.
*   **Seguridad:** Especialmente en lo que respecta a las credenciales y el aislamiento.
*   **Rendimiento:** Para la eficiencia del flujo de trabajo del desarrollador.
*   **Mantenibilidad:** De la configuración y las herramientas del entorno.
*   **Compatibilidad Multiplataforma:** Una consideración importante para la configuración de Docker.
## Evaluación de la Plantilla de Inicio

### Dominio Tecnológico Principal

El dominio principal es un **Entorno de Desarrollo Full-Stack**, diseñado para ser una base estandarizada y reproducible para proyectos de Odoo.

### Pila Tecnológica Seleccionada

Nuestra 'plantilla de inicio' se define por la siguiente pila de tecnologías base, seleccionada para garantizar la estabilidad, compatibilidad y una experiencia de desarrollo moderna.

**Decisiones Arquitectónicas Proporcionadas por la Pila:**

**Aplicación y Runtime:**
*   **Odoo:** Versión **17**, la última versión estable soportada.
*   **Python:** Versión **3.10**, cumpliendo con los requisitos de Odoo 17.

**Base de Datos:**
*   **PostgreSQL:** Versión **12**, la versión recomendada para Odoo 17 para máxima estabilidad.

**Contenerización y Orquestación:**
*   **Plataforma:** **Docker** con **Docker Compose** para definir y ejecutar el entorno multi-contenedor (Odoo, PostgreSQL).
*   **Integración IDE:** **VS Code Dev Containers** para una experiencia de desarrollo fluida y una configuración consistente.

**Entorno de Desarrollo y Herramientas:**
*   **Usuario y Grupo:** Se creará un usuario (`odoo`) y un grupo (`odoo`) dedicados y sin privilegios de root para poseer los archivos de la aplicación y ejecutar el proceso de Odoo, mejorando la seguridad.
*   **Shell por Defecto:** El shell por defecto para el usuario `odoo` será `Zsh`, proporcionando una interfaz de línea de comandos más potente y amigable.
*   **Mejoras de la Terminal:** Se instalará `Oh My Zsh`, junto con los plugins `zsh-autosuggestions` y `zsh-syntax-highlighting`, para mejorar la productividad y la experiencia del desarrollador en la terminal dentro del contenedor.
*   **Permisos:** El usuario y grupo `odoo` tendrán la propiedad y los permisos adecuados sobre el código fuente de Odoo y los directorios de addons personalizados, garantizando el acceso de lectura/escritura/ejecución donde sea necesario.

**Rationale for Selection:**
Esta configuración proporciona una base robusta, segura y altamente productiva para el desarrollo de Odoo. Sigue las mejores prácticas de la industria al utilizar contenedores, ejecutar procesos sin privilegios de root y mejorar la experiencia del desarrollador con herramientas modernas. Las versiones de la tecnología principal se eligen para garantizar la máxima compatibilidad y estabilidad según la documentación oficial de Odoo.
## Core Architectural Decisions

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**
*   **Pila Tecnológica Fundamental:** Odoo 17, Python 3.10, PostgreSQL 12.
*   **Contenerización:** Docker y VS Code Dev Containers.
*   **Usuario y Entorno de Shell:** Usuario y grupo `odoo`, Zsh con Oh My Zsh.

**Important Decisions (Shape Architecture):**
*   **Estrategia de Migración/Actualización de Módulos Odoo:** Herramientas de migración nativas de Odoo (`--update` / `post-init` / `pre-init` hooks).
*   **Resolución de Dominio Local / Proxy Inverso:** Traefik Proxy.
*   **Recarga en Caliente/Recarga en Vivo de Addons de Odoo:** Opciones nativas de Odoo (`--dev=all` o `--reload`).
*   **Estrategia de Gestión de Addons Personalizados:** Volúmenes montados desde el host.
*   **Estrategia de Gestión de Configuración Extendida:** Combinación de `odoo.conf` y variables de entorno.
*   **Estrategia de Registro y Depuración:** Salida directa a consola (Docker Logs) y depurador de VS Code.
*   **Gestión Segura de Credenciales de Git:** Reenvío del Agente SSH (SSH Agent Forwarding).

**Decisiones Diferidas (Post-MVP):**
(Ninguna decisión explícitamente diferida en esta etapa, ya que estamos centrados en la definición del entorno de desarrollo.)

### Arquitectura de Datos

*   **Decisión:** Estrategia de Migración/Actualización de Módulos Odoo.
*   **Elección:** Herramientas de migración nativas de Odoo (`--update` / `post-init` / `pre-init` hooks).
*   **Razón:** Enfoque idiomático y mantenible, integrado con el ciclo de vida de los módulos de Odoo, asegura la coherencia.

### Autenticación y Seguridad
*   **Decisión:** Gestión Segura de Credenciales de Git.
*   **Elección:** Reenvío del Agente SSH (SSH Agent Forwarding).
*   **Razón:** Permite el uso de claves SSH del host de forma segura dentro del contenedor sin almacenarlas, cumpliendo con el RNF3.

### Patrones de API y Comunicación
(No decisiones adicionales tomadas en esta categoría, ya que Odoo define sus propias APIs.)

### Arquitectura Frontend
(No aplicable, ya que Odoo tiene su propio frontend.)

### Infraestructura y Despliegue

*   **Decisión:** Resolución de Dominio Local / Proxy Inverso.
*   **Elección:** Traefik Proxy.
*   **Razón:** Automatización, excelente integración con Docker, gestiona nombres de dominio personalizados y múltiples proyectos eficientemente, aborda RF17.
*   **Decisión:** Recarga en Caliente/Recarga en Vivo de Addons de Odoo.
*   **Elección:** Opciones nativas de Odoo (`--dev=all` o `--reload`).
*   **Razón:** Soporte nativo, aborda directamente RF6 para retroalimentación inmediata, se integra perfectamente con el flujo de desarrollo de Odoo.
*   **Decisión:** Estrategia de Gestión de Addons Personalizados.
*   **Elección:** Volúmenes montados desde el host.
*   **Razón:** Soporta iteración rápida, permite el uso del IDE del host, funciona bien con la recarga en caliente.
*   **Decisión:** Estrategia de Gestión de Configuración Extendida.
*   **Elección:** Enfoque híbrido: `odoo.conf` para ajustes específicos de Odoo, variables de entorno para detalles específicos de Docker/Dev Container.
*   **Razón:** Flexible, robusto, aprovecha la configuración nativa de Odoo y las variables de entorno estándar de los contenedores.
*   **Decisión:** Estrategia de Registro y Depuración.
*   **Elección:** Salida directa a consola (Docker Logs) y depurador de VS Code.
*   **Razón:** Simplicidad, monitorización en tiempo real, práctica estándar de Docker, se integra con el depurador de VS Code.

### Análisis del Impacto de las Decisiones

**Secuencia de Implementación:**
1.  Configuración de la pila tecnológica fundamental (Odoo, Python, PostgreSQL).
2.  Implementación de Docker y VS Code Dev Containers.
3.  Configuración de usuario y grupo `odoo`, Zsh y sus plugins.
4.  Configuración de Traefik Proxy para resolución de dominios.
5.  Configuración de Odoo para recarga en caliente (`--dev=all`).
6.  Definición de volúmenes montados para addons personalizados.
7.  Implementación de la gestión de configuración híbrida (`odoo.conf` y variables de entorno).
8.  Configuración del registro de Odoo a `stdout` para Docker logs y uso del depurador de VS Code.

**Dependencias entre Componentes:**
*   La elección de Docker y Dev Containers es fundamental para todas las demás decisiones de infraestructura.
*   La recarga en caliente depende directamente de los volúmenes montados para addons.
*   El proxy Traefik dependerá de la configuración de red de Docker Compose y los labels en el servicio Odoo.
*   La gestión de configuración afectará tanto al `odoo.conf` como a las variables de entorno de Docker Compose/Dev Container.
*   El usuario `odoo` y la configuración de Zsh afectarán directamente el `Dockerfile` y la experiencia de desarrollo dentro del contenedor.
## Implementation Patterns & Consistency Rules

### Pattern Categories Defined

**Puntos de Conflicto Críticos Identificados:**
4 áreas donde los agentes de IA podrían tomar decisiones diferentes que causarían conflictos.

### Patrones de Nomenclatura

**Convenciones de Nomenclatura de Bases de Datos:**
(No se definieron decisiones adicionales explícitas aquí, ya que Odoo gestiona gran parte de esto y la nomenclatura de tablas/columnas está implícita por el ORM y las convenciones de `snake_case` de Python.)

**Convenciones de Nomenclatura de API:**
(No se definieron decisiones adicionales explícitas aquí, ya que Odoo define sus propias APIs).

**Convenciones de Nomenclatura de Código:**
*   **Regla:** Utilizar **Snake_case** para nombres de archivos y directorios de módulos de Odoo, variables y funciones en Python (siguiendo PEP 8).
*   **Ejemplo:** `mi_modulo_personalizado`, `mi_archivo_modelo.py`, `calcular_total()`, `mi_variable_local`.

### Patrones de Estructura

**Organización del Proyecto:**
*   **Regla:** Adherirse estrictamente a la **Estructura Estándar de Módulos Odoo** (`models/`, `views/`, `wizards/`, `reports/`, `security/`, `data/`, `static/`, `controllers/`, etc.).
*   **Razón:** Asegura la compatibilidad con los mecanismos de carga de Odoo y facilita la comprensión por parte de cualquier desarrollador de Odoo.

**Patrones de Estructura de Archivos:**
*   **Regla:** Ubicar las pruebas para los módulos de Odoo en un **subdirectorio `tests/`** dentro de cada módulo (`tests/test_*.py`).
*   **Razón:** Práctica estándar de Odoo, permite el descubrimiento automático por el ejecutor de pruebas nativo.

### Patrones de Formato

**Formatos de Respuesta de API:**
(No se definieron decisiones adicionales explícitas aquí, ya que Odoo define sus propios formatos de respuesta).

**Formatos de Intercambio de Datos:**
(No se definieron decisiones adicionales explícitas aquí, implícitas por Odoo y Python).

### Patrones de Comunicación

**Patrones del Sistema de Eventos:**
(No se definieron decisiones adicionales explícitas aquí, ya que Odoo tiene su propio sistema de eventos).

**Patrones de Gestión de Estado:**
(No se definieron decisiones adicionales explícitas aquí, ya que Odoo tiene su propia gestión de estado a través del ORM y la lógica de negocio).

### Patrones de Proceso

**Patrones de Manejo de Errores:**
(Las decisiones sobre patrones específicos de manejo de errores aún no se han tomado, pero el enfoque de registro definido ayudará en este aspecto).

**Patrones de Estados de Carga:**
(Las decisiones sobre patrones específicos de estados de carga aún no se han tomado, ya que típicamente son manejados por el frontend de Odoo).

**Proceso de Creación de Módulos:**
*   **Regla:** La creación de la estructura básica de nuevos módulos de Odoo debe realizarse utilizando el **comando `scaffold` de Odoo**, preferiblemente encapsulado en un script de conveniencia.
*   **Razón:** Asegura una estructura estándar, consistente y actualizada, y cumple con el RF11.

### Directrices de Cumplimiento

**Todos los Agentes de IA DEBEN:**
*   Seguir las convenciones de nomenclatura **Snake_case** para archivos, directorios, variables y funciones en Python.
*   Adherirse a la **Estructura Estándar de Módulos Odoo** (`models/`, `views/`, etc.).
*   Ubicar los archivos de prueba en el **subdirectorio `tests/`** dentro de cada módulo.
*   Utilizar el **comando `scaffold` de Odoo** (vía script) para la creación de nuevos módulos.
*   Emplear el **sistema de logging nativo de Odoo y Python** con un uso consistente de los niveles de registro (`info`, `warning`, `error`).

**Aplicación de Patrones:**
*   **Verificación:** A través de revisiones de código y posiblemente herramientas de linting configuradas para las convenciones establecidas.
*   **Documentación de Violaciones:** Las violaciones se registrarán en los comentarios de las revisiones de código o en las herramientas de análisis estático.
*   **Proceso de Actualización de Patrones:** Cualquier cambio en estos patrones requerirá una discusión colaborativa y aprobación explícita del equipo de arquitectura.

### Ejemplos de Patrones

**Buenos Ejemplos:**
*   `mi_modulo_personalizado/models/mi_modelo.py`
*   `mi_modulo_personalizado/tests/test_mi_modelo.py`
*   `_logger.info("Registro de evento con nivel informativo.")`
*   Comando para crear un módulo (vía script): `python odoo-bin scaffold mi_nuevo_modulo ./custom_addons`

**Anti-Patrones:**
*   `MiCustomModule/Models/MiModel.py` (CamelCase, PascalCase para archivos/directorios).
*   Pruebas ubicadas fuera de `tests/`.
*   Uso inconsistente de `_logger.debug` para información crítica.
## Project Structure & Boundaries

### Complete Project Directory Structure
```
odoo-env/
├── .devcontainer/                         # Configuración de VS Code Dev Container
│   ├── devcontainer.json                  # Configuración de VS Code Dev Container, extensiones, puertos
│   ├── docker-compose.yml                 # Servicios de Docker Compose para Odoo, PostgreSQL, Traefik
│   ├── .env.example                       # Ejemplo de variables de entorno
│   ├── build/                             # Scripts/assets para la construcción del Dockerfile
│   │   ├── Dockerfile                     # Dockerfile personalizado para el servicio Odoo (usuario, zsh, plugins)
│   │   ├── entrypoint.sh                  # Script de entrada personalizado para el servicio Odoo
│   │   └── wait-for-psql.py               # Utilidad para esperar a PostgreSQL
│   ├── config/                            # Configuración específica de Odoo
│   │   └── odoo.conf                      # Archivo de configuración de Odoo (montado en el contenedor)
│   ├── addons/                            # Volumen montado desde el host para módulos Odoo personalizados
│   │   └── my_first_module/               # Ejemplo de módulo Odoo (snake_case)
│   │       ├── __init__.py
│   │       ├── __manifest__.py
│   │       ├── models/
│   │       ├── views/
│   │       ├── security/
│   │       └── tests/
│   └── scripts/                           # Scripts personalizados para el flujo de trabajo de desarrollo
│       ├── create_module.sh               # Wrapper para `odoo-bin scaffold`
│       └── update_modules.sh              # Wrapper para `odoo-bin --update all`
├── .env                                   # Variables de entorno (ignoradas por Git)
├── .gitignore                             # Reglas de ignorado de Git
├── README.md                              # Descripción general del proyecto, configuración, uso
├── docs/                                  # Documentación del proyecto
│   └── architecture.md                    # Nuestro documento de arquitectura
└── .vscode/                               # Configuración específica de VS Code
    ├── launch.json                        # Configuraciones de depuración para Python/Odoo
    └── settings.json
```

### Architectural Boundaries

**API Boundaries:**
Odoo's internal XML-RPC/JSON-RPC/ORM APIs. Traefik will expose Odoo's web interface.

**Component Boundaries:**
Odoo modules as the primary components, communicating via Odoo's ORM and business logic. Docker containers define service boundaries (Odoo, PostgreSQL, Traefik).

**Service Boundaries:**
(Same as Component Boundaries in this context)

**Data Boundaries:**
PostgreSQL database for Odoo's data. `odoo-env` only manages the *environment* for this data, not its internal structure directly (Odoo ORM handles that).

### Requirements to Structure Mapping

**Feature/Epic Mapping:**
*   **RF1-RF5 (Environment Lifecycle & Config):** `.devcontainer/docker-compose.yml`, `.devcontainer/build/Dockerfile`, `.devcontainer/devcontainer.json`, `.env.example`, `.env`, `.devcontainer/config/odoo.conf`.
*   **RF6-RF9 (Integrated Dev Experience):** `.devcontainer/devcontainer.json` (debugger, extensions), `.devcontainer/addons/` (mounted), `.devcontainer/scripts/` (for `odoo-bin` wrappers), `odoo.conf` (for hot-reloading `--dev=all`).
*   **RF10-RF12 (Tools & Automation):** `.devcontainer/devcontainer.json` (extensions), `.devcontainer/scripts/create_module.sh`, `.devcontainer/scripts/update_modules.sh`.
*   **RF13-RF15 (Documentation & Onboarding):** `README.md`, `docs/` directory.
*   **RF16-RF19 (Operations & Prod Parity):** `docker-compose.yml` (Traefik, networking), `.gitignore`, overall Docker structure.

### Integration Points

**Internal Communication:**
Odoo modules communicate via Odoo's ORM and business logic. Docker services (Odoo, PostgreSQL, Traefik) communicate over a dedicated Docker network.

**External Integrations:**
None defined in the MVP.

**Data Flow:**
User interacts with Odoo -> Odoo container processes request -> Odoo container communicates with PostgreSQL container for data persistence -> Response sent back to user.

### File Organization Patterns

**Configuration Files:**
`devcontainer.json`, `docker-compose.yml`, `build/Dockerfile` in `.devcontainer/`. `odoo.conf` in `.devcontainer/config/`. `.env` files in root. `launch.json` and `settings.json` in `.vscode/`.

**Source Organization:**
Custom Odoo modules will live in `.devcontainer/addons/`.

**Test Organization:**
Each module will have its own `tests/` subdirectory.

**Asset Organization:**
Static assets for Odoo modules will live in `static/` subdirectories within each module, as per Odoo's standard structure.

### Development Workflow Integration

**Development Server Structure:**
The structure is designed for use with VS Code Dev Containers. Opening the project in a Dev Container will automatically start all services.

**Build Process Structure:**
The build process is managed by `docker-compose build` and `devcontainer up`, which uses the `Dockerfile` in `.devcontainer/build/`.

**Deployment Structure:**
The Docker-based structure (`docker-compose.yml`, `Dockerfile`) provides a strong foundation for creating production-ready images and CI/CD pipelines.
## Architecture Validation Results

### Coherence Validation ✅

**Decision Compatibility:**
All technology choices (Odoo 17, Python 3.10, PostgreSQL 12, Docker, Traefik, Zsh) are compatible and work together cohesively.

**Pattern Consistency:**
The chosen implementation patterns (Snake_case, Standard Odoo Structure, `scaffold` command) are consistent with the technology stack and Odoo best practices.

**Structure Alignment:**
The project structure directly supports all architectural decisions, providing clear locations for container configuration, custom addons, and scripts.

### Requirements Coverage Validation ✅

**Functional Requirements Coverage:**
All 19 Functional Requirements from the PRD are architecturally supported by the combination of Docker, Dev Containers, Odoo's native features, and the defined project structure.

**Non-Functional Requirements Coverage:**
All NFRs are addressed, including performance (via compatible versions), security (via non-root user and SSH agent forwarding), scalability (via containerization), and reliability (via stable versions).

### Implementation Readiness Validation ✅

**Decision Completeness:**
All critical decisions are documented with versions and rationale, providing a clear guide for implementation.

**Structure Completeness:**
The project structure is specific and complete, defining the location of all key files and directories.

**Pattern Completeness:**
Core patterns for naming, structure, testing, and logging have been defined to ensure consistency.

### Gap Analysis Results

*   **Identified Gap:** The initial architecture lacked a specific plan for RNF3 (Secure Git Credential Management).
*   **Resolution:** The gap was addressed by adding **SSH Agent Forwarding** as a core security decision.

### Architecture Completeness Checklist

**✅ Requirements Analysis**

- [x] Project context thoroughly analyzed
- [x] Scale and complexity assessed
- [x] Technical constraints identified
- [x] Cross-cutting concerns mapped

**✅ Architectural Decisions**

- [x] Critical decisions documented with versions
- [x] Technology stack fully specified
- [x] Integration patterns defined
- [x] Performance considerations addressed

**✅ Implementation Patterns**

- [x] Naming conventions established
- [x] Structure patterns defined
- [x] Communication patterns specified
- [x] Process patterns documented

**✅ Project Structure**

- [x] Complete directory structure defined
- [x] Component boundaries established
- [x] Integration points mapped
- [x] Requirements to structure mapping complete

### Architecture Readiness Assessment

**Overall Status:** READY FOR IMPLEMENTATION

**Confidence Level:** High

**Key Strengths:**
*   **Reproducibility:** The Docker and Dev Container setup ensures a consistent environment for all developers.
*   **Developer Experience:** Features like hot-reloading, Zsh, and script wrappers will significantly improve developer productivity.
*   **Security:** The use of a non-root user and SSH Agent Forwarding follows security best practices.
*   **Clarity:** The structure and patterns are well-defined and follow industry standards.

**Areas for Future Enhancement:**
*   Formalizing CI/CD pipeline configuration based on the development environment.
*   Developing more comprehensive custom scripts for automating common tasks.

### Implementation Handoff

**AI Agent Guidelines:**
- Follow all architectural decisions exactly as documented.
- Use implementation patterns consistently across all components.
- Respect the project structure and boundaries.
- Refer to this document for all architectural questions.

**First Implementation Priority:**
The first priority is to create the physical project structure and the configuration files within the `.devcontainer/` directory (`devcontainer.json`, `docker-compose.yml`, `build/Dockerfile`, `config/odoo.conf`, etc.) to enable the Dev Container environment.