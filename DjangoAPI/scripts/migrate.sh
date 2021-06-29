cd /var/www/DjangoApp
source /var/www/DjangoApp -myenv/bin/activate
DJANGO_SETTINGS_MODULE=DjangoApp/DjangoAPI/DjangoAPI/settings RDS_DB_NAME=django-project RDS_DB_USER=django_admin RDS_DB_PASSWD=athena.s RDS_HOST=django-project.cbhwp3yflsbx.us-east-1.rds.amazonaws.com RDS_PORT=3306 ./manage.py makemigrations
DJANGO_SETTINGS_MODULE=DjangoApp/DjangoAPI/DjangoAPI/settings RDS_DB_NAME=django-project RDS_DB_USER=django_admin RDS_DB_PASSWD=athena.s RDS_HOST=django-project.cbhwp3yflsbx.us-east-1.rds.amazonaws.com RDS_PORT=3306 ./manage.py migrate auth
DJANGO_SETTINGS_MODULE=DjangoApp/DjangoAPI/DjangoAPI/settings RDS_DB_NAME=django-project RDS_DB_USER=django_admin RDS_DB_PASSWD=athena.s RDS_HOST=django-project.cbhwp3yflsbx.us-east-1.rds.amazonaws.com RDS_PORT=3306 ./manage.py migrate
