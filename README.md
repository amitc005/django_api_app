# API web app using Django and its plugins

## List of Plugins

1. Django Rest framework
2. Django Rest Auth
3. All Auth
4. drf-yasg - Yet another Swagger generator

### Installation Steps:

- Create python virtual environment.
  - `$ python -m venv .env`
- Enable virtual environment.
  - `$ source .env/bin/activate`
- Run Migration
  - `(.env) $ python manage.py migrate`
- Run Server
  - `python manage.py runserver`

### Important Urls:

- Server URL: http://127.0.0.1:8000/
- Swagger docs: http://127.0.0.1:8000/docs/
- redoc docs: http://127.0.0.1:8000/redoc
