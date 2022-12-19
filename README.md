# Insurance API
A place for insurance services of Insurance API

## TL;DR

We're using:

- [DJANGO](https://www.djangoproject.com/)
- [DJANGO-FILTER](https://django-filter.readthedocs.io/en/stable/) for filtering.
- [DJANGO-REST-FRAMEWORK](https://www.django-rest-framework.org/) for the API development

### Quickstart
 
* Run `Insurance`

1. Create a virtualenv
    ```
    python3.9 -m venv {env_location}
    ```
2. Activate the venv
    ```
    source {env_location}/bin/activate
    ```
3. Install the minimum requirements
    ```
    pip install -r requirements/base.txt
    ```
4. Create a `.env` file with needed environmental variables by copying the example
    ```
    cp .env-example .env
    ```
5. Load your `.env` file
    ```
    set -a && source .env && set +a
    ```
6. Migrate the database
   ```
   python manage.py migrate
   ```
   
7. Run the application
    ```
    python manage.py runserver
    ```


To run tests you can

```
pytest -v
```

