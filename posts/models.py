from django.db import models
from django.contrib.postgres.fields import JSONField

class Post(models.Model):
  text  = models.TextField()
  comments = JSONField(null=True, blank=True, verbose_name='Comments')

  def __str__(self):
    """A string representation of the model """
    return self.text
