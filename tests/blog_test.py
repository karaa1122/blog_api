from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Blog


class BlogViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create some test blogs
        Blog.objects.create(user=self.user, title='Test Blog 1', blog_text='Lorem ipsum dolor sit amet')
        Blog.objects.create(user=self.user, title='Test Blog 2', blog_text='Consectetur adipiscing elit')
        # ...

    def test_get_list(self):
        url = 'blog/blog/' 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_blog(self):
        url = 'blog/blog/'  
        data = {
            'title': 'New Blog',
            'blog_text': 'This is a new blog',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
