from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import Stock, Holding

class HoldingViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('user', 'user@example.com', 'password')
        self.stock = Stock.objects.create(name="Apple", symbol="AAPL", latest_price=150.00)
        self.holding = Holding.objects.create(user=self.user, stock=self.stock, quantity=10)
        self.client.login(username='user', password='password')

    def test_view_holdings(self):
        response = self.client.get(reverse('holding-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['stock']['name'], 'Apple')
        self.assertEqual(response.data[0]['quantity'], 10)
