# Project Overview - odoo-env

## Executive Summary

The `odoo-env` project is designed as a robust and reproducible development environment for Odoo applications. It leverages Docker and Docker Compose to create a consistent local setup, including the Odoo application server and a PostgreSQL database. The current codebase primarily focuses on environment configuration, with no custom Odoo modules or direct extensions detected in the specified `addons` directory.

## Technology Stack

*   **Primary Language:** Python
*   **Framework:** Odoo
*   **Database:** PostgreSQL
*   **Containerization:** Docker, Docker Compose

## Architecture Type

The project's underlying Odoo framework inherently follows a **Service/API-centric** architectural pattern, where functionalities are often exposed through modular services and APIs. The project structure itself is a **Monolith** in terms of repository organization, containing all components within a single repository.

## Repository Structure

The project is structured as a **Monolith**, with all development environment configurations and potential Odoo module development managed within this single repository.

## Detailed Documentation Links

For more in-depth information, please refer to the following documents:

*   [Arquitectura del Proyecto](./architecture.md)
*   [Análisis del Árbol de Código Fuente](./source-tree-analysis.md)
*   [Guía de Desarrollo](./development-guide.md)
*   [Guía de Despliegue](./deployment-guide.md)
*   [Contratos API](./api-contracts-main.md)
*   [Modelos de Datos](./data-models-main.md)
*   [Análisis exhaustivo](./comprehensive-analysis-main.md)
*   [Inventario de Componentes](./component-inventory.md)
*   [Guía de Contribución](./contribution-guide.md)