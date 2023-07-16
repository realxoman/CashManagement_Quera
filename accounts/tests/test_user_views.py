from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        return super().setUp()

    def test_list_users(self):
        url = reverse('accounts:users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse('accounts:users-list')
        data = {
            'username': 'newuser',
            'password': 'newpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 2)

    def test_balance(self):
        url = reverse('accounts:users-balance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_balance(self):
        self.client.logout()  # Logout to make the request unauthenticated
        url = reverse('accounts:users-balance')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
