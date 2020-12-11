web: gunicorn project.wsgi --log-file -
web: python manage.py runserver 0.0.0.0:$PORT --noreload
gunicorn==20.0.4