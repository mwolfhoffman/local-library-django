# Library

Django application that creates a Library with Books to be checked out.

## To Install
1. `python3 -m venv venv`
1. `source venv/bin/activate`
1. `python manage.py makemigrations`
1. `python manage.py migrate`

## To Run

1.  `python manage.py runserver`

## To Test

1.  `python manage.py test`

## To Deploy On Railway

1. `prep-deploy-railway.sh`
1. Follow instructions [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

## Add Books, Authors, etc

1.  `python manage.py createsuperuser`
1.  Navigate to `localhost:8000/admin`
