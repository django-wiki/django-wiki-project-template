#!/bin/sh
pip install -r requirements/base.txt
python manage.py syncdb
python manage.py migrate
