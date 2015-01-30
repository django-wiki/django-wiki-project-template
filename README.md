# Project template for django-wiki

This project template aims to be an easy way to get a wiki up and running using
the awesome django-wiki (http://django-wiki.org)

# Usage

Start a project like this:

    django-admin.py startproject --template=https://github.com/django-wiki/django-wiki-project-template/archive/master.zip <project_name>

Now make sure you have everything installed in your virtualenv (you are using
virtualenv right!?):

    pip install -r requirements/base.txt

Then go sync and migrate the database:

    ./manage.py syncdb; ./manage.py migrate

Now you are ready to go!


# Setting structure

This project template tries to encourage "The One True Way" of doing settings
in Django (http://2scoops.co/the-best-and-worst-of-django slide 51). So the
basic settings are in <project_name>/settings/base.py.
The manage.py script has also been edited to reflect this.

But hey, if you don't like it, then just change it ;)
