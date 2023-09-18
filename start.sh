#!/usr/bin/env bash

sleep 1

python manage.py makemigrations --settings=bitpin.production_settings &&
python manage.py migrate --settings=bitpin.production_settings
python manage.py collectstatic --no-input

gunicorn bitpin.wsgi:application --bind 0.0.0.0:8000 -w 2
