#!/usr/bin/env bash

sleep 1

python manage.py makemigrations &&
python manage.py migrate --settings=bitpin.product_settings

gunicorn bitpin.asgi:application --bind 0.0.0.0:8000 -w 2 -k uvicorn.workers.UvicornWorker
