from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse





class RegisterViewTest(APITestCase):
    def test_register_valid_data(self):
        url = 'blog/register'  
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'account is created')
        

    def test_register_invalid_data(self):
        url = 'blog/register'  
        data = {
            'username': 'testuser',
            'email': 'invalid_email', 
            'password': 'testpassword'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'something went wrong')


