# Django Blog 
Django tutorial project

## Setup

1. Create virtual environment:
    ```
    python3 -m venv venv
    ```
    Windows:
    ```
    py -m venv venv
    ```

2. Activate environment:
    ```
    source venv/bin/activate
    ```
    Windows:
    ```
    source venv/Scripts/activate
    ```

3. Install requirements:
    ```
    pip install -r requirements.txt
    ```

4. Create database and update database settings (in settings.py); or use dafault sqlite3 database

5. Generate a new secret key. The quickest way is to use Django Secret Key Generatos like [djecrety](https://djecrety.ir/)

6. Make & run migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    Windows
    ```
    py manage.py makemigrations
    py manage.py migrate
    ```

7. If app has a custom user model - create a new superuser for the admin:
    ```
    python manage.py createsuperuser
    ```
    Windows
    ```
    py manage.py createsuperuser
    ```

8. Start the development server:
    ```
    python manage.py runserver
    ```
    Windows
    ```
    py manage.py runserver
    ```