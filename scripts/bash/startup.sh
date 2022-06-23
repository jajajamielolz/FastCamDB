#!/usr/bin/env bash

for id in $(docker ps -q)
do
    if [[ $(docker port "${id}") == *"5432"* ]] || [[ $(docker port "${id}") == *"6379"* ]] || [[ $(docker port "${id}") == *"8000"* ]] || [[ $(docker port "${id}") == *"8001"* ]]; then
        echo "stopping container ${id}"
        docker stop "${id}"
    fi
done

docker-compose --env-file .env.local -f fastcam-docker-compose.yml up -d