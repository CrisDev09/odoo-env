# Arquitectura del Proyecto Odoo-env

## Resumen Ejecutivo

Este documento describe la arquitectura actual del proyecto 'odoo-env'. Principalmente, configura un entorno de desarrollo para Odoo (Python/PostgreSQL) utilizando Docker y Docker Compose para garantizar la reproducibilidad. El análisis del código no reveló módulos Odoo personalizados ni extensiones directas dentro de la estructura actual del proyecto.

## Pila Tecnológica

*   **Lenguaje de Programación:** Python
*   **Framework:** Odoo
*   **Base de Datos:** PostgreSQL
*   **Contenerización:** Docker, Docker Compose

## Patrón Arquitectónico

El proyecto sigue un patrón arquitectónico **servicio/API-céntrico**, que es inherente al framework Odoo. Odoo es un sistema modular, pero en la configuración actual, no se han detectado módulos personalizados adicionales.

## Arquitectura de Datos

La arquitectura de datos se basa en PostgreSQL, que es la base de datos relacional estándar utilizada por Odoo.

*   **Modelos de Datos:** No se encontraron modelos de datos Odoo personalizados en el directorio `addons`. El proyecto utiliza los modelos de datos integrados de Odoo.
*   **Documentación Detallada:** Consulte [Data Models - Main Project](./data-models-main.md) para más detalles.

## Diseño de API

Odoo proporciona una API HTTP que sus módulos pueden extender.

*   **Controladores API:** No se encontraron controladores de API personalizados en el directorio `addons`. El proyecto utiliza las APIs integradas de Odoo.
*   **Documentación Detallada:** Consulte [API Contracts - Main Project](./api-contracts-main.md) para más detalles.

## Visión General de Componentes

No se han identificado componentes personalizados del lado de Odoo en este proyecto. La estructura se centra en la configuración del entorno para Odoo.

## Árbol de Código Fuente

Para una descripción detallada de la estructura de directorios y la ubicación de los archivos clave, consulte [Análisis del Árbol de Directorios Fuente](./source-tree-analysis.md).

## Flujo de Trabajo de Desarrollo

El flujo de trabajo de desarrollo se centra en el uso de contenedores Docker para un entorno consistente y reproducible.

*   **Documentación Detallada:** Consulte [Guía de Desarrollo](./development-guide.md) para instrucciones detalladas sobre la configuración y el desarrollo.

## Arquitectura de Despliegue

La arquitectura de despliegue se basa en Docker Compose para orquestar los servicios de la aplicación Odoo y su base de datos PostgreSQL.

*   **Componentes:** Un servicio `web` para Odoo y un servicio `db` para PostgreSQL, definidos en `docker-compose.yml`.
*   **Configuración:** Definida en `.devcontainer/config/odoo.conf` y `docker-compose.yml`.
*   **Documentación Detallada:** Consulte [Guía de Despliegue](./deployment-guide.md) para una descripción completa.

## Estrategia de Pruebas

No se detectaron pruebas personalizadas en el directorio `addons`. La estrategia de pruebas dependerá de la implementación de módulos personalizados y podría utilizar los mecanismos de prueba integrados de Odoo o frameworks de prueba de Python.