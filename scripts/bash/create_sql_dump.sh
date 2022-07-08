#!/bin/bash
# Creates a dump file of current db state
source .env.development

local_file="./scripts/bash/fast_cam_db_dump_$(date +"%T").sql"

echo "Creating a local dump of fast cam db"
PGPASSWORD=$DB_SUPERPASSWORD pg_dump -h $DB_HOSTNAME -U $DB_SUPERUSER -f $local_file $DB_DATABASE
