#!/usr/bin/env bash
cd /var/www/project/
source /var/www/DjangoApp/DjangoAPI/myenv/bin/activate
python manage.py runserver
