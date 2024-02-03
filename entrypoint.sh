#!/bin/bash

set -e 

source /env/bin/activate


if [$l == 'gunicorn']; then 

    exec gunicorn django_invoice.wsgi:application -b 0.0.0.0:8000
else
    exec python manage.py runserver 0.0.0.0:8000

fi