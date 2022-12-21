#!/bin/sh

python manage.py flush --no-input --settings project.dev
python manage.py makemigrations --settings project.dev
python manage.py migrate --settings project.dev

exec "$@"