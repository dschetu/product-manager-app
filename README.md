# product-manager-app

create a virtual environment using the below code
python -m venv env'

activate the environment

install django and djangorestframeowrk using below commands
pip install django
pip install djangorestframework

create a project by using below command
django-admin startproject promanage

create a application within django framework
django-admin startapp products

whenever we create models so we need to run makemigartion command in order to create necessary tables
python manage.py makemigrations products
python manage.py migrate products

Register application within django settings file, also include 'rest_framework' app within settings.py file

to run server use command
python manage.py runserver
