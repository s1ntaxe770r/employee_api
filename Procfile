web: gunicorn emp.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py makemigrations
python manage.py migrate