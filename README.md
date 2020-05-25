# Email message sending via Gmail using Django server on GCP

### This example simple send a mail in the specified email address

## 1) Clone the ansible script on your local machine

git clone https://github.com/amardrylab/ansible_djangoserver3.git

## 2) Change directory and start the ansible-playbook

- cd ansible_djangoserver3
- ansible-playbook instance_create.yml

## 3) SSH to your created machine

ssh www.drylab.in

## 4) Create your virtual environment

virtualenv myproject

## 5) Install git software

- sudo apt-get install git

## 6) Clone the django scripts

 git clone https://github.com/amardrylab/django-email.git


## 7) Copy the required files in proper location

mv django-email/*  myproject

## 8) Enter your virtual environment

- source myproject/bin/activate
- cd myproject

## 9) Install the required softwares in the local environment

- pip install django

## 10) Change the settings.py in myproject directory

- vi myproject/settings.py

and then put your email address and password

## 11) Restart the services

- sudo service nginx restart
- sudo service uwsgi restart
