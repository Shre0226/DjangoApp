#!/usr/bin/env bash
cd /home/ec2-user/www/project/
source /home/ec2-user/www/code-deploy/DjangoAPI/myenv/bin/activate
python manage.py runserver
