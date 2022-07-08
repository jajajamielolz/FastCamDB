#!/bin/bash
# loads most recent dump file into empty db

source .env.development

echo 'Closing all active connections to destination database'
PGPASSWORD=$DB_SUPERPASSWORD psql -h $DB_HOSTNAME -U $DB_SUPERUSER -d $DB_DATABASE -c "SELECT pid, pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = current_database() AND pid <> pg_backend_pid();"

echo 'Removing old destination database'
PGPASSWORD=$DB_SUPERPASSWORD psql -h $DB_HOSTNAME -U $DB_SUPERUSER -d postgres -c "DROP DATABASE IF EXISTS $DB_DATABASE;"

echo 'Creating a new destination database'
PGPASSWORD=$DB_SUPERPASSWORD psql -h $DB_HOSTNAME -U $DB_SUPERUSER -d postgres -c "CREATE DATABASE $DB_DATABASE"

echo 'Selecting most recent dump file'
export local_file=./scripts/bash/$(ls -t ./scripts/bash  | grep fast | head -1)

echo "Importing dump file to destination db: $DB_HOSTNAME"
PGPASSWORD=$DB_SUPERPASSWORD psql -h $DB_HOSTNAME -U $DB_SUPERUSER -d $DB_DATABASE -f $local_file

echo 'running alembic migration to head...'
ENVIRONMENT=development alembic upgrade head
source venv/bin/activate
echo 'running db_setup script...'
ENVIRONMENT=development python3 scripts/db_setup.py