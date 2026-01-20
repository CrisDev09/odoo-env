#!/usr/bin/env python3
import os
import sys
import time
import psycopg2

# Obtiene la configuración de la base de datos desde variables de entorno
db_host = os.environ.get("POSTGRES_HOST")
db_port = os.environ.get("POSTGRES_PORT")
db_user = os.environ.get("POSTGRES_USER")
db_password = os.environ.get("POSTGRES_PASSWORD")
db_name = os.environ.get("POSTGRES_DB")

if not all([db_host, db_port, db_user, db_password, db_name]):
    print("Error: Una o más variables de entorno de la base de datos no están definidas.", file=sys.stderr)
    print("Asegúrate de que POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, y POSTGRES_DB están definidas.", file=sys.stderr)
    sys.exit(1)

# Número máximo de intentos y tiempo de espera
max_attempts = 30
wait_seconds = 2

def check_postgres():
    """Intenta conectarse a PostgreSQL en un bucle."""
    for i in range(max_attempts):
        try:
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
                connect_timeout=3
            )
            conn.close()
            print("PostgreSQL está listo para aceptar conexiones.")
            return True
        except psycopg2.OperationalError as e:
            print(f"Intento {i + 1}/{max_attempts}: PostgreSQL no está listo aún. Esperando...")
            print(f"Error: {e}")
            time.sleep(wait_seconds)
    return False

if __name__ == "__main__":
    if not check_postgres():
        print("No se pudo conectar a PostgreSQL después de varios intentos. Abortando.", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)