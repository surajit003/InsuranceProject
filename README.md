# Insurance API
A place for insurance services of Insurance API

## TL;DR

We're using:

- [DJANGO](https://www.djangoproject.com/)
- [DJANGO-FILTER](https://django-filter.readthedocs.io/en/stable/) for filtering.
- [DJANGO-REST-FRAMEWORK](https://www.django-rest-framework.org/) for the API development

### Quickstart


```
create a .env file at the root folder 
copy the values from .env-example to .env

create virtualenvironment
virtualenv env

activate virtualenv
source env/bin/activate
```

Install

* pip install -r requirements/base.txt
* python manage.py migrate
* python manage.py runserver


To run tests you can

```
pytest -v
```

