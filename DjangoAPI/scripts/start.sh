#!/usr/bin/env bash
cd /home/ec2-user/var/www/
source /myenv/bin/activate
python manage.py runserver
