from django.test import SimpleTestCase
from django.http import HttpRequest, HttpResponse
from django.urls import reverse

# from pages import views

class HomePageTests(SimpleTestCase):
  def test_home_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('home'))
    self.assertEquals(response.status_code, 200)
  
  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('home'))
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')
  
  def test_home_page_contains_correct_html(self):
    response =  self.client.get('/')
    self.assertContains(response, '<h1>Homepage</h1>')
  
  def test_home_page_does_not_contain_incorrect_html(self):
    response = self.client.get('/')
    self.assertNotContains(response, 'Not supposed to be on the page')

class AboutPageTest(SimpleTestCase):
  def setUp(self):
    self.response = self.client.get('/about/')

  def test_about_page_status_code(self):
    self.assertEquals(self.response.status_code, HttpResponse.status_code)
  
  def test_get_url_by_name(self):
    response = self.client.get(reverse('about'))
    self.assertEquals(response.status_code, HttpResponse.status_code)
  
  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('about'))
    self.assertTemplateUsed(response, 'about.html')
  

  def test_about_page_contains_correct_content(self):
    self.assertContains(self.response, '<h1>About page</h1>')

  def test_about_page_does_not_contain_incorrect_content(self):
    self.assertNotContains(self.response, 'Should not be found')