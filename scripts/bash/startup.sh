#!/usr/bin/env bash

# stop any containers running on required ports
for id in $(docker ps -q)
do
    if [[ $(docker port "${id}") == *"5432"* ]] || [[ $(docker port "${id}") == *"6379"* ]] || [[ $(docker port "${id}") == *"8000"* ]] || [[ $(docker port "${id}") == *"8001"* ]]; then
        echo "stopping container ${id}"
        docker stop "${id}"
    fi
done

# start up FastCamDB, redis, and postgres
docker-compose --env-file .env.local -f fastcam-docker-compose.yml up -d