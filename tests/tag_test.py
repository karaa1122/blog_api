
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Tags



       
class TagviewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

       
        Tags.objects.create(name='Tag 1')
        Tags.objects.create(name='Tag 2')
 

    def test_get_list(self):
        url = '/blog/tags/' 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_create_tag(self):
        url = '/blog/tags/'  
        data = {
            'name': 'New Tag',
            
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      
