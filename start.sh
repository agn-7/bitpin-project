#!/usr/bin/env bash

cd ./bitpin

python3 manage.py makemigrations &&
python3 manage.py migrate

gunicorn bitpin.wsgi:application --bind 0.0.0.0:8000 -w 2
