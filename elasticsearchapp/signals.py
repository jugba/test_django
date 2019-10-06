from posts.models import Post
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Post, dispatch_uid='elasticsearchapp.signals.index_post')
def index_post(sender, instance, **kwargs):    
  _index(instance)

def _index(ins):
  ins.indexing()