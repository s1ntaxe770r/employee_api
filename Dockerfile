FROM python:3.8.2-alpine3.10 

ADD . .

RUN source env/bin/activate

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000","emp.wsgi"]

