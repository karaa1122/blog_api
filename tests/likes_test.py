from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Likes
from blog.serializers import LikesSerializer


class LikeViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.likes_data = {'user': self.user.id, 'post': 1}  
        self.url = reverse('likes-list')  

    def test_create_like(self):
        response = self.client.post(self.url, self.likes_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Likes.objects.count(), 1)
        self.assertEqual(response.data, LikesSerializer(Likes.objects.first()).data)

    def test_get_like_list(self):
        Likes.objects.create(user=self.user, post=1) 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user.id)
        self.assertEqual(response.data[0]['post'], 1)

    def test_delete_like(self):
        like = Likes.objects.create(user=self.user, post=1)  
        delete_url = reverse('likes-detail', args=[like.id])  
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Likes.objects.count(), 0)
