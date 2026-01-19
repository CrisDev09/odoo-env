---
stepsCompleted: ['step-01-validate-prerequisites', 'step-02-design-epics', 'step-03-create-stories']
inputDocuments:
  - doc_output/planning-artifacts/prd.md
  - doc_output/planning-artifacts/architecture.md
---

# odoo-env - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for odoo-env, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

- **RF1 (Inicialización del Entorno):** Un **Desarrollador** puede inicializar y lanzar el entorno completo (Odoo, DB) abriendo el proyecto en VS Code y seleccionando "Reopen in Container".
- **RF2 (Configuración de Versión):** Un **Desarrollador** puede configurar la versión de Odoo a través de una variable de entorno (`.env`).
- **RF3 (Configuración de Proyecto):** Un **Desarrollador** puede configurar los ajustes del proyecto (nombre, credenciales DB) a través de variables de entorno.
- **RF4 (Gestión de Dependencias)::** El **Sistema** gestiona las dependencias base de Python (`Dockerfile`). Un **Desarrollador** puede añadir paquetes suplementarios vía `requirements.txt`.
- **RF5 (Aislamiento):** El **Sistema** aísla todas las dependencias y servicios en contenedores Docker.
- **RF6 (Edición de Addons):** Un **Desarrollador** puede editar `addons` locales con cambios reflejados inmediatamente en el contenedor.
- **RF7 (Depuración):** Un **Desarrollador** puede depurar tanto el código de sus `addons` como el código nativo de Odoo utilizando configuraciones predefinidas en VS Code (`launch.json`).
- **RF8 (Navegación de Código):** Un **Desarrollador** puede ver y navegar por el código fuente nativo de Odoo en VS Code dentro del Dev Container.
- **RF9 (Ejecución de Pruebas):** Un **Desarrollador** puede ejecutar pruebas unitarias para sus módulos desde la terminal del Dev Container.
- **RF10 (Extensiones IDE):** El **Sistema** instala automáticamente extensiones esenciales de VS Code (ej. Python, linters) al iniciar el Dev Container.
- **RF11 (Creación de Módulos):** Un **Desarrollador** puede usar un script para crear la estructura básica de un nuevo módulo de Odoo.
- **RF12 (Actualización de Módulos):** Un **Desarrollador** puede usar un script para actualizar módulos en la instancia de Odoo en ejecución.
- **RF13 (Guía Principal):** Un **Desarrollador** puede consultar un `README.md` completo (instalación, configuración, uso).
- **RF14 (Solución de Problemas):** Un **Desarrollador** puede consultar una guía de solución de problemas para errores comunes.
- **RF15 (Ejemplos):** Un **Desarrollador** puede consultar ejemplos de código (módulo Odoo, script de prueba).
- **RF16 (Base para CI/CD):** Un **Ingeniero de DevOps** puede usar la configuración del entorno para construir pipelines de CI/CD e imágenes de producción.
- **RF17 (Proxy Inverso):** El **Sistema** soporta la resolución de dominios locales (ej. `project1-odoo.com`) al contenedor de Odoo, vía proxy inverso.
- **RF18 (Gestión de Secretos):** El **Sistema** evita la confirmación de secretos en el repositorio (`.env` en `.gitignore`).
- **RF19 (Compatibilidad):** El **Sistema** garantiza un comportamiento consistente en los principales sistemas operativos anfitriones.

### NonFunctional Requirements

- **RNF1:** Inicialización del Dev Container: < 2 minutos (post-construcción).
- **RNF2:** Interacciones básicas en Odoo: Tiempos de carga < 3 segundos.
- **RNF3:** Gestión de Credenciales de Git: Mecanismo seguro (ej. reenvío SSH-Agent) desde el contenedor, sin almacenar en texto plano.
- **RNF4:** Uso Concurrente: Soporte para 10-15 desarrolladores ejecutando instancias en una máquina estándar sin degradación significativa.
- **RNF5:** Estabilidad: Funcionamiento consistente durante jornada laboral de 8 horas sin reinicios frecuentes.

### Additional Requirements

- **Pila Tecnológica Fundamental:** Odoo 17, Python 3.10, PostgreSQL 12.
- **Contenerización:** Docker y VS Code Dev Containers.
- **Usuario y Entorno de Shell:** Usuario y grupo `odoo` no-root, Zsh con Oh My Zsh y plugins (`zsh-autosuggestions`, `zsh-syntax-highlighting`).
- **Proxy Inverso para Dominios Locales:** Traefik Proxy.
- **Recarga en Caliente de Addons:** Opciones nativas de Odoo (`--dev=all` o `--reload`).
- **Gestión de Addons Personalizados:** Volúmenes montados desde el host.
- **Gestión de Configuración:** Enfoque híbrido (`odoo.conf` y variables de entorno).
- **Registro y Depuración:** Salida a consola (Docker Logs) e integración con el depurador de VS Code.
- **Gestión de Credenciales de Git:** Reenvío del Agente SSH (SSH Agent Forwarding).
- **Creación de Módulos:** Usar el comando `scaffold` de Odoo, encapsulado en un script.
- **Estructura del Proyecto:** Adherirse a la estructura estándar de módulos de Odoo y la estructura de directorios definida en el documento de arquitectura.
- **Convenciones de Código:** Usar `snake_case` para archivos, directorios, variables y funciones.

### FR Coverage Map

FR1: Epic 1 - Entorno de Desarrollo Fundamental
FR2: Epic 1 - Entorno de Desarrollo Fundamental
FR3: Epic 1 - Entorno de Desarrollo Fundamental
FR4: Epic 1 - Entorno de Desarrollo Fundamental
FR5: Epic 1 - Entorno de Desarrollo Fundamental
FR10: Epic 1 - Entorno de Desarrollo Fundamental
FR19: Epic 1 - Entorno de Desarrollo Fundamental
FR6: Epic 2 - Flujo de Trabajo de Desarrollo Acelerado
FR7: Epic 2 - Flujo de Trabajo de Desarrollo Acelerado
FR8: Epic 2 - Flujo de Trabajo de Desarrollo Acelerado
FR9: Epic 2 - Flujo de Trabajo de Desarrollo Acelerado
FR11: Epic 3 - Gestión del Ciclo de Vida de los Módulos
FR12: Epic 3 - Gestión del Ciclo de Vida de los Módulos
FR16: Epic 4 - Paridad con Producción y Operaciones
FR17: Epic 4 - Paridad con Producción y Operaciones
FR18: Epic 4 - Paridad con Producción y Operaciones
FR13: Epic 5 - Documentación y Soporte al Desarrollador
FR14: Epic 5 - Documentación y Soporte al Desarrollador
FR15: Epic 5 - Documentación y Soporte al Desarrollador

## Epic List

### Epic 1: Entorno de Desarrollo Fundamental
Un desarrollador puede lanzar un entorno Odoo completamente funcional, aislado y preconfigurado con un solo comando, listo para el desarrollo.
**FRs cubiertos:** RF1, RF2, RF3, RF4, RF5, RF10, RF19.

### Epic 2: Flujo de Trabajo de Desarrollo Acelerado
Un desarrollador puede editar código de addons personalizados, ver los cambios reflejados al instante (hot-reload), y depurar tanto su código como el núcleo de Odoo usando VS Code.
**FRs cubiertos:** RF6, RF7, RF8, RF9.

### Epic 3: Gestión del Ciclo de Vida de los Módulos
Un desarrollador puede crear la estructura de un nuevo módulo de Odoo y actualizar los módulos existentes en la instancia en ejecución utilizando scripts de ayuda.
**FRs cubiertos:** RF11, RF12.

### Epic 4: Paridad con Producción y Operaciones
Un ingeniero de DevOps puede usar la configuración como base para CI/CD, y un desarrollador puede usar dominios locales (ej. `mi-proyecto.odoo.test`) para acceder a su instancia. Se asegura la gestión de secretos.
**FRs cubiertos:** RF16, RF17, RF18.

### Epic 5: Documentación y Soporte al Desarrollador
Un desarrollador tiene acceso a una guía completa para la instalación, configuración, uso y solución de problemas comunes, incluyendo ejemplos.
**FRs cubiertos:** RF13, RF14, RF15.

### Story 1.1: Lanzamiento del Entorno Básico

Como un Desarrollador,
quiero lanzar los servicios de Odoo y la base de datos usando un solo comando,
para que pueda tener un entorno base funcional.

**Acceptance Criteria:**

**Dado que** tengo Docker y VS Code instalados,
**Cuando** ejecuto el comando "Reopen in Container" desde VS Code,
**Entonces** se crean y se inician sin errores un contenedor de Odoo y un contenedor de PostgreSQL.
**Y** los registros (logs) del contenedor de Odoo indican que el servidor se ha iniciado correctamente y está listo para aceptar conexiones.

### Story 1.2: Configuración del Entorno

Como un Desarrollador,
quiero configurar la versión de Odoo, las credenciales de la base de datos y los nombres de los contenedores usando un archivo de entorno,
para que pueda adaptar el entorno y evitar conflictos con otros proyectos.

**Acceptance Criteria:**

**Dado que** tengo un entorno ejecutándose desde la Historia 1.1,
**Y** tengo un archivo `.env` con las variables `ODOO_VERSION`, `POSTGRES_PASSWORD` y una variable para el nombre del proyecto (ej. `PROJECT_NAME`),
**Cuando** reconstruyo y lanzo el contenedor a través de "Reopen in Container",
**Entonces** la instancia de Odoo utiliza la versión especificada.
**Y** el contenedor de Odoo se conecta a la base de datos utilizando las credenciales especificadas.
**Y** los contenedores de Docker creados se nombran usando la variable `PROJECT_NAME` para asegurar su unicidad (ej. `mi-proyecto_odoo_1`, `mi-proyecto_db_1`).

### Story 1.3: Gestión de Dependencias de Python

Como un Desarrollador,
quiero añadir paquetes de Python suplementarios al entorno de Odoo usando un archivo `requirements.txt`,
para que mis módulos de Odoo personalizados puedan usar librerías de terceros.

**Acceptance Criteria:**

**Dado que** tengo un entorno ejecutándose,
**Y** tengo un archivo `requirements.txt` en la ubicación designada del proyecto (ej. en `.devcontainer/build/`),
**Y** he añadido un nuevo paquete de Python (ej. `requests`) a este archivo `requirements.txt`,
**Cuando** reconstruyo el Dev Container,
**Entonces** el nuevo paquete de Python se instala y está disponible para importar dentro del entorno de Python del contenedor de Odoo.

### Story 1.4: Instalación Automática de Extensiones de VS Code

Como un Desarrollador,
quiero que las extensiones esenciales de VS Code se instalen automáticamente al iniciar el Dev Container,
para que mi IDE esté inmediatamente listo para el desarrollo de Odoo sin configuración manual.

**Acceptance Criteria:**

**Dado que** mi archivo `devcontainer.json` especifica una lista de extensiones recomendadas (ej. Python, Docker, etc.),
**Cuando** lanzo el Dev Container por primera vez o después de una reconstrucción,
**Entonces** todas las extensiones especificadas se instalan y activan dentro de mi instancia de VS Code conectada al contenedor.

### Story 1.5: Consistencia Multiplataforma

Como un Arquitecto de Sistemas,
quiero que la configuración del entorno se base en características de Docker compatibles con múltiples plataformas,
para que los desarrolladores en Windows, macOS y Linux tengan una experiencia de desarrollo consistente y fiable.

**Acceptance Criteria:**

**Dado que** la documentación del proyecto incluye detalles sobre la compatibilidad con plataformas,
**Cuando** reviso los archivos `docker-compose.yml` y `Dockerfile`,
**Entonces** utilizan características estándar de Docker y mejores prácticas que se sabe que funcionan consistentemente en Windows, macOS y Linux.
**Y** el `README.md` especifica claramente las versiones mínimas requeridas de Docker Desktop/Engine y Docker Compose para cada sistema operativo compatible.

### Story 2.1: Desarrollo de Addons Locales con Recarga en Caliente (Hot-Reload)

Como un Desarrollador,
quiero editar los módulos de mis addons locales en mi máquina anfitriona y que los cambios se reflejen inmediatamente en el contenedor en ejecución,
para que pueda iterar en el desarrollo rápidamente.

**Acceptance Criteria:**

**Dado que** el entorno está en ejecución y tengo un directorio local de `addons` montado como un volumen en el contenedor de Odoo,
**Cuando** hago un cambio en un archivo de Python dentro de un módulo de addon local,
**Entonces** el servidor de Odoo que se ejecuta dentro del contenedor se recarga automáticamente para aplicar el cambio.
**Y** cuando hago un cambio en un archivo de vista XML, el cambio es visible en la interfaz de usuario de Odoo después de una actualización del navegador (y potencialmente actualizando el módulo en la interfaz de usuario).

### Story 2.2: Depuración del Código de Addons Personalizados

Como un Desarrollador,
quiero depurar solamente el código de mis addons personalizados,
para que pueda diagnosticar rápidamente los problemas sin entrar en el código del framework de Odoo a menos que yo lo decida.

**Acceptance Criteria:**

**Dado que** existe una configuración en `launch.json` llamada "Debug Odoo (Mi Código)",
**Cuando** lanzo esta sesión de depuración,
**Entonces** el servidor de Odoo se inicia.
**Y** el depurador solo se detiene en los puntos de interrupción establecidos dentro del directorio de mis addons personalizados (respetando la configuración `justMyCode: true`).
**Y** el depurador *no* se detiene en puntos de interrupción en el código fuente nativo de Odoo.

### Story 2.3: Depuración de Todo el Código (Personalizado + Núcleo de Odoo)

Como un Desarrollador,
quiero una configuración de depuración separada para recorrer tanto mi código personalizado como el código del framework de Odoo,
para que pueda realizar un análisis profundo y entender la pila de llamadas completa.

**Acceptance Criteria:**

**Dado que** existe una configuración en `launch.json` llamada "Debug Odoo (All Code)",
**Cuando** lanzo esta sesión de depuración,
**Entonces** el servidor de Odoo se inicia.
**Y** el depurador se detiene en los puntos de interrupción establecidos dentro del directorio de mis addons personalizados.
**Y** también se detiene en los puntos de interrupción establecidos dentro del código fuente nativo de Odoo (respetando la configuración `justMyCode: false`).

### Story 2.4: Navegación y Búsqueda en el Código Nativo de Odoo

Como un **Desarrollador**,
quiero poder navegar, buscar y ver las definiciones del código fuente nativo de Odoo directamente en mi editor,
para que pueda entender cómo funciona el framework, usar sus APIs correctamente y depurar problemas de manera más eficiente.

**Criterios de Aceptación:**

**Dado que** estoy dentro del Dev Container en VS Code,
**Cuando** abro un archivo de Python de mis addons personalizados,
**Y** hago clic en una función o clase del núcleo de Odoo (ej. `self.env['res.partner']`),
**Entonces** soy llevado inmediatamente a la definición de esa clase o función en el código fuente nativo de Odoo.
**Y** puedo realizar búsquedas de texto completo en todo el código fuente de Odoo y obtener resultados.

### Story 2.5: Ejecución de Pruebas Unitarias desde la Terminal

Como un **Desarrollador**,
quiero poder ejecutar las pruebas unitarias para un módulo específico directamente desde la terminal del Dev Container,
para que pueda verificar la correctitud de mi código antes de integrarlo en un flujo de CI/CD.

**Criterios de Aceptación:**

**Dado que** estoy en la terminal del Dev Container,
**Cuando** ejecuto el comando de pruebas de Odoo apuntando a uno de mis módulos personalizados (ej. `odoo -c /etc/odoo/odoo.conf -i mi_modulo --test-enable`),
**Entonces** se ejecuta el conjunto de pruebas para "mi_modulo".
**Y** la salida en la terminal muestra un resumen de las pruebas ejecutadas, indicando cuántas pasaron y cuántas fallaron.
**Y** el proceso de Odoo termina con un código de salida 0 si todas las pruebas pasan, o un código distinto de 0 si alguna falla.

### Story 2.6: Depuración de Pruebas Unitarias mediante VS Code

Como un **Desarrollador**,
quiero una configuración de depuración predefinida en VS Code para iniciar Odoo en modo de prueba para un módulo específico,
para poder depurar mis pruebas unitarias de forma eficiente y analizar el flujo de ejecución de mi código de prueba junto con el de Odoo.

**Criterios de Aceptación:**

**Dado que** existe una configuración en `launch.json` llamada "Debug Odoo Tests (My Module)",
**Cuando** lanzo esta configuración de depuración,
**Entonces** el servidor de Odoo se inicia en modo de prueba (`--test-enable`) y con el depurador de Python (`debugpy`) adjunto.
**Y** puedo configurar esta configuración para que ejecute las pruebas de un módulo específico (ej. "mi_modulo") o todos los módulos instalados.
**Y** el depurador se detiene en los puntos de interrupción establecidos tanto en mi código de prueba como en el código del módulo bajo prueba.

### Story 3.1: Creación de un Nuevo Módulo de Odoo

Como un **Desarrollador**,
quiero poder ejecutar un script Bash que me guíe en la creación de la estructura básica de un nuevo módulo de Odoo,
para que pueda iniciar rápidamente el desarrollo de nuevas funcionalidades siguiendo las convenciones del proyecto.

**Criterios de Aceptación:**

**Dado que** estoy en la terminal del Dev Container,
**Cuando** ejecuto el script de creación de módulos (ej. `./scripts/create_module.sh`) y proporciono el nombre del nuevo módulo,
**Entonces** el script utiliza el comando `scaffold` de Odoo para generar la estructura básica del módulo en la ubicación designada para addons personalizados.
**Y** el nuevo módulo incluye los archivos esenciales (`__init__.py`, `__manifest__.py`, `models/`, `views/`, `security/`).
**Y** el `__manifest__.py` está pre-rellenado con la información básica (nombre, versión, autor).

### Story 3.2: Actualización de Módulos de Odoo en Ejecución

Como un **Desarrollador**,
quiero poder ejecutar un script Bash para actualizar módulos específicos en la instancia de Odoo que está en ejecución en el Dev Container,
para que los cambios en mi código o en los datos de manifest se apliquen sin tener que reiniciar todo el entorno manualmente.

**Criterios de Aceptación:**

**Dado que** la instancia de Odoo está en ejecución en el Dev Container,
**Y** he modificado el código o el `__manifest__.py` de un módulo,
**Cuando** ejecuto el script de actualización de módulos (ej. `./scripts/update_module.sh mi_modulo`),
**Entonces** el script ejecuta el comando de actualización de Odoo (`-u mi_modulo`) para el módulo especificado.
**Y** los cambios se aplican correctamente en la instancia de Odoo.
**Y** la operación se completa con éxito y se informa al usuario del resultado.

### Story 4.1: Gestión Segura de Secretos y Configuración

Como un **Desarrollador**,
quiero que la configuración sensible, como las contraseñas, se gestione a través de un archivo `.env` que esté excluido del control de versiones,
para que no se confirmen accidentalmente secretos en el repositorio de código.

**Criterios de Aceptación:**

**Dado que** el proyecto tiene un archivo `.gitignore`,
**Cuando** reviso el contenido del archivo `.gitignore`,
**Entonces** la entrada `.env` está presente.
**Y** en el archivo `docker-compose.yml`, los servicios que requieren secretos (como la base de datos) los cargan desde el archivo `.env`.

### Story 4.2: Dominios Locales con Proxy Inverso

Como un **Desarrollador**,
quiero poder acceder a mi instancia de Odoo en ejecución a través de un dominio local amigable (ej. `mi-proyecto.odoo.test`),
para que pueda simular un entorno de producción y trabajar con múltiples proyectos sin colisiones de puertos.

**Criterios de Aceptación:**

**Dado que** el entorno está configurado con un proxy inverso (como Traefik),
**Y** he configurado mi máquina anfitriona para resolver `mi-proyecto.odoo.test` a `127.0.0.1`,
**Cuando** navego a `http://mi-proyecto.odoo.test` en mi navegador,
**Entonces** se muestra la interfaz de inicio de sesión de mi instancia de Odoo en ejecución.

### Story 4.3: Base para Integración Continua (CI)

Como un **Ingeniero de DevOps**,
quiero que la configuración del entorno sea una base sólida para construir imágenes de Docker para CI/CD,
para que pueda asegurar la paridad entre los entornos de desarrollo, pruebas y producción.

**Criterios de Aceptación:**

**Dado que** existe un `Dockerfile` en el proyecto que define la imagen base de Odoo,
**Cuando** un pipeline de CI lo utiliza para construir una imagen de Docker,
**Entonces** la imagen se construye correctamente sin errores.
**Y** el proceso de CI puede integrar los addons personalizados en la imagen final de producción de manera eficiente (ya sea copiándolos o montándolos desde una fuente controlada), asegurando que la imagen resultante sea un artefacto autocontenido y versionado.

### Story 5.1: Guía Completa de Instalación y Uso

Como un **Desarrollador**,
quiero tener acceso a un archivo `README.md` completo y bien estructurado,
para que pueda instalar, configurar y comenzar a usar el entorno de desarrollo de Odoo de forma autónoma.

**Criterios de Aceptación:**

**Dado que** accedo al `README.md` principal del proyecto,
**Entonces** el `README.md` incluye secciones claras sobre:
*   Pre-requisitos de software (Docker, VS Code).
*   Pasos de instalación detallados para diferentes sistemas operativos.
*   Instrucciones de configuración inicial (ej. archivo `.env`).
*   Comandos básicos para iniciar, detener y reconstruir el entorno.
*   Una guía rápida de inicio para desarrollar un módulo Odoo.
*   Cómo usar las herramientas del Dev Container (depuración, tests, etc.).

### Story 5.2: Guía de Solución de Problemas Comunes

Como un **Desarrollador**,
quiero tener acceso a una guía de solución de problemas para errores comunes,
para que pueda resolver rápidamente los inconvenientes sin tener que buscar ayuda externa o invertir mucho tiempo.

**Criterios de Aceptación:**

**Dado que** me encuentro con un problema común durante el desarrollo (ej. "el contenedor no arranca", "no veo mis cambios en Odoo"),
**Cuando** consulto la sección de solución de problemas en la documentación del proyecto (ej. en el `README.md` o un documento dedicado),
**Entonces** encuentro una lista de los problemas más frecuentes con sus posibles causas y soluciones claras y concisas.

### Story 5.3: Ejemplos de Código y Uso

Como un **Desarrollador**,
quiero tener acceso a ejemplos de código bien documentados,
para que pueda entender cómo estructurar mi código y cómo usar las funcionalidades clave del entorno.

**Criterios de Aceptación:**

**Dado que** estoy desarrollando un nuevo módulo de Odoo o un script para el entorno,
**Cuando** consulto la sección de ejemplos en la documentación,
**Entonces** encuentro:
*   Un módulo de Odoo de ejemplo (simple, con un modelo, una vista y un menú).
*   Un script de prueba de ejemplo para un módulo de Odoo.
*   Un script Bash de utilidad (ej. de los que hemos definido para la creación o actualización de módulos).
**Y** cada ejemplo está acompañado de una breve explicación de su propósito y cómo usarlo.