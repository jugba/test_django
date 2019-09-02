from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
  return x + y

@periodic_task(
  run_every=(crontab(minute='*/2')),
  name='task_run_every_2_mins'
)
def task_run_every_two_mins():
  logger.info('task completed')
  return 2
