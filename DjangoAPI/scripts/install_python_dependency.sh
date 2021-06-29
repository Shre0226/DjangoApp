#!/usr/bin/env bash
sudo su
yum update -y
yum install httpd
service httpd start
chkconfig httpd on
yum install -y python3
yum install httpd-devel
yum install -y mod_wsgi
pip3 install django==2.1.1
pip3 install django-cors-headers
pip3 install djangorestframework
pip3 install virtualenv
cd /var/www/
chown ec2-user:ec2-user /var/www/
chown ec2-user:ec2-user /var/www/DjangoApp/DjangoAPI/myenv/
chown ec2-user:ec2-user /var/www/DjangoApp/DjangoAPI/myenv/*
source /var/www/DjangoApp/DjangoAPI/myenv/bin/activate

