#!/bin/bash
# Scrip para automatizar las migraciones de django y mantener servidor 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000