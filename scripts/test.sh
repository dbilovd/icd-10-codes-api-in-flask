#!/bin/sh
cd .devops/docker
docker-compose exec -e FLASK_ENV="testing" web python manage.py test