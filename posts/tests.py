import json

from django.test import TestCase
from django.urls import reverse

from posts.models import Post

class PostTests(TestCase):

  def setUp(self):
    Post.objects.create(text='just a test', comments=[{"text": 'valid'}])

  def test_text_content(self):
    post =  Post.objects.get(id=1)
    expected_object_name = f'{post.text}'
    self.assertEquals(expected_object_name, 'just a test')
  
  def test_post_list_view(self):
    response =  self.client.get(reverse('posts'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'just a test')
    self.assertTemplateUsed(response, 'posts.html')
  
  def test_post_str(self):
    post  = Post.objects.all()[0]
    text = post.__str__()
    self.assertEquals(text, 'just a test')
  
  def test_post_comments(self):
    post = Post.objects.get(id=1)
    comments = post.comments
    self.assertEquals(len(comments), 1)