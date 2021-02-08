#!/bin/sh
cd .devops/docker
docker-compose exec web python manage.py test