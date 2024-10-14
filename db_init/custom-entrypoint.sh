#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
until pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB"; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Run the initialization script
if [ -f "/docker-entrypoint-initdb.d/init.sql" ]; then
  psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /docker-entrypoint-initdb.d/init.sql || true
fi

# Execute the default entrypoint command
exec "$@"
