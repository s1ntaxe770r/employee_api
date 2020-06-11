web: gunicorn emp.wsgi
python manage.py collectstatic --noinput
manage.py makemigrations
python manage.py migrate