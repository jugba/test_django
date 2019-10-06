[![CircleCI](https://circleci.com/gh/jugba/test_django.svg?style=svg)](https://circleci.com/gh/jugba/test_django)

## Installation

- pip install -r requirements.txt

## migrate and connect db
- python manage.py migrate

- python manage.py runserver


## Run Celery worker
celery -A myproject worker -l info

## Run Celery beat
celery -A myproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Download and extract elastic search
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.1.tar.gz
- extract
  tar -xzf elasticsearch-5.1.1.tar.gz
  
##Start ElasticSearch
./elasticsearch-5.1.1/bin/elasticsearch


## Run test
python manage.py run

