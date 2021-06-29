#!/usr/bin/env bash
sudo su
yum update -y
yum install httpd
service httpd start
chkconfig httpd on
cd /var/www/
chown ec2-user:ec2-user /var/www/
chown ec2-user:ec2-user /var/www/DjangoApp/DjangoAPI/myenv/
chown ec2-user:ec2-user /var/www/DjangoApp/DjangoAPI/myenv/*
source /var/www/DjangoApp/DjangoAPI/myenv/bin/activate
pip install -r /var/www/DjangoApp/DjangoAPI/requirements.txt
