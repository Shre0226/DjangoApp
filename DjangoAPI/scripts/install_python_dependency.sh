#!/usr/bin/env bash
sudo apt-get install libmysqlclient-dev
sudo yum install -y mysql-devel
sudo yum install psycopg2
chown ec2-user:ec2-user /home/ec2-user/www
chown ec2-user:ec2-user /home/ec2-user/www/code-deploy/DjangoAPI/myenv
chown ec2-user:ec2-user /home/ec2-user/www/code-deploy/DjangoAPI/myenv/*
source /home/ec2-user/www/code-deploy/DjangoAPI/myenv/bin/activate
pip install -r /home/ec2-user/www/code-deploy/DjangoAPI/requirements.txt
