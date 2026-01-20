#!/bin/bash
set -e

# Espera a que la base de datos esté lista
/usr/local/bin/wait-for-psql.py

# Si el primer argumento es 'odoo', ejecuta Odoo.
# De lo contrario, ejecuta el comando que se pasó.
if [ "$1" = 'odoo' ]; then
    shift
    exec odoo "$@"
else
    exec "$@"
fi