from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch


connections.create_connection()

class BlogPostIndex(DocType): 
  posted_date = Date()    
  text = Text()
  title = Text()    
  class Meta:        
    index = 'blogpost-index'

def bulk_indexing():   
  from posts import models 
  BlogPostIndex.init()    
  es = Elasticsearch()    
  bulk(client=es, actions=(b.indexing() for b in models.Post.objects.all().iterator()))

def search(title):    
  s = Search().filter('term', title=title)    
  response = s.execute()    
  return response