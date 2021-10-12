# experiment-django-with-fastapi
Tryout django orm and fastapi for API

- run FastAPI
    ```commandline
    poetry run uvicorn mysite.asgi:application --port 8001 --reload
    ```
  
- run django for convenience
    ```commandline
    poetry run python manage.py runserver  # default on port 8000
    ```
  
- API docs: http://localhost:8001/docs
- Django admin: http://localhost:8000/admin
