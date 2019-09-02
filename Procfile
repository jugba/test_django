web: gunicorn myproject.wsgi
worker: celery -A myproject worker -l info -B
release: python manage.py migrate
