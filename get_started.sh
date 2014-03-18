#!/bin/sh
pip install -r requirements/base.txt
./manage.py syncdb
./manage.py migrate
