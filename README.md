#Installation

>pip install -r requirements.txt

##migrate and connect db
>python manage.py migrate

>python manage.py runserver


## Run Celery worker
celery -A myproject worker -l info

## Run Celery beat
celery -A myproject beat -l info

##Start ElasticSearch
./elasticsearch-5.1.1/bin/elasticsearch

