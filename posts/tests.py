import json

from django.test import TestCase
from django.urls import reverse
import mock

from posts.models import Post

class PostTests(TestCase):

  def setUp(self):
    Post.objects.create(title="news", text="just a test", comments=[{"text": 'valid'}])

  @mock.patch('elasitcsearchapp.signals.index_post')
  def test_text_content(self,mock_post_save):
    post =  Post.objects.get(id=1)
    expected_object_name = f'{post.text}'
    self.assertTrue(mock_post_save.called, 'Failed to save post to Elastic Search')
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