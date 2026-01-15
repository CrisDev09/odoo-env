# Development Guide - Main Project

This guide provides instructions for setting up and working with the `odoo-env` development environment.

## Prerequisites

*   **Docker**: Ensure Docker Desktop (or Docker Engine) is installed and running on your system.
*   **Docker Compose**: Docker Compose is typically bundled with Docker Desktop.
*   **Git**: For cloning the repository.

## Local Environment Setup

The project uses a Docker-based development environment to ensure reproducibility.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd odoo-env
    ```
2.  **Start the development environment:**
    Navigate to the `.devcontainer` directory and start the Docker services:
    ```bash
    cd .devcontainer
    docker-compose up -d
    ```
    This will build the Odoo image (if not already built) and start the Odoo and PostgreSQL containers.

3.  **Access Odoo:**
    Once the containers are up, Odoo should be accessible via your browser, typically at `http://localhost:8069`.

## Running Odoo Commands

To execute Odoo commands (e.g., updating modules, running tests) within the running container:
```bash
docker-compose exec odoo odoo -c /etc/odoo/odoo.conf -d <database-name> <command-options>
```
For example, to update a module:
```bash
docker-compose exec odoo odoo -c /etc/odoo/odoo.conf -d my_database -u my_module
```

## Environment Configuration

*   **Odoo Configuration**: The primary Odoo configuration is located at `.devcontainer/config/odoo.conf`.
*   **Environment Variables**: Specific environment variables for Docker Compose services might be defined within `.devcontainer/.env` (if present) or directly in `docker-compose.yml`.

## Custom Module Development

Custom Odoo modules are expected to be placed in the `.devcontainer/addons` directory. Any new modules added there will be automatically picked up by Odoo on restart or module update.

## Testing

Testing is typically performed using Odoo's built-in test mechanisms or Python testing frameworks like `pytest` within the Odoo container. Specific test commands for this project are not explicitly defined in the scanned files.