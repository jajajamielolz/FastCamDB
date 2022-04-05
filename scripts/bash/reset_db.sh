# Run in base_fast_repo directory (working directory)
echo  'restting db...'
echo 'working directory:' "$(pwd)"
source venv/bin/activate
echo 'removing postgres docker container...'
docker rm -f fast-cam-postgres
echo 'removing postgres docker volume...'
docker volume rm vol_fast-cam-postgres
echo 're-composing docker...'
docker-compose --env-file .env."$ENVIRONMENT" -f fastcam-docker-compose.yml up -d --build postgressql
# If no sleep psycopg2 connection will terminate.
# potentially some process is not being finished before command execution
sleep 1
echo 'running alembic migration to head...'
alembic upgrade head
echo 'running db_setup script...'
python3 scripts/db_setup.py