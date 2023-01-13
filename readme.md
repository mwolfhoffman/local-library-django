# Library

Django application that creates a Library with Books, Authors, and BookInstances that can be checked out.

## To Install

1. Clone repo
1. `python3 -m venv venv`
1. `source venv/bin/activate`
1. `python manage.py makemigrations`
1. `python manage.py migrate`

## To Run
1.  `python manage.py runserver`

## To Test
1.  `python manage.py test`

## To Deploy
1. `python3 manage.py check --deploy`
1. Follow instructions [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment) or [here](https://docs.djangoproject.com/en/4.0/howto/deployment/).

## Add Books, Authors, etc
1.  `python manage.py createsuperuser`
1. Navigate to `localhost:8000/admin`

