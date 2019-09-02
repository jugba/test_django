from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from elasticsearchapp.search import BlogPostIndex
class Post(models.Model):
  title = models.CharField(max_length=200, blank=True, null=True)
  text  = models.TextField()
  comments = JSONField(null=True, blank=True, verbose_name='Comments')
  posted_date = models.DateField(default=timezone.now)

  def __str__(self):
    """A string representation of the model """
    return self.text
  
  def indexing(self):   
    obj = BlogPostIndex(      
      meta={'id': self.id},      
      posted_date=self.posted_date,      
      title=self.title,      
      text=self.text   
      )   
    obj.save()   
    return obj.to_dict(include_meta=True)
