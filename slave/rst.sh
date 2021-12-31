#!/bin/sh
docker-compose -f /home/slave/project/docker-compose.yaml stop
docker-compose -f /home/slave/project/docker-compose.yaml rm -f
docker-compose -f /home/slave/project/docker-compose.yaml pull
docker-compose -f /home/slave/project/docker-compose.yaml up -d
