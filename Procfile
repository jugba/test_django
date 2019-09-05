web: gunicorn myproject.wsgi
worker: celery -A myproject worker -l info -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
release: python manage.py migrate
