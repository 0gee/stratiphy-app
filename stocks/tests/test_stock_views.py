from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..models import Stock
from ..serializers import StockSerializer
from django.contrib.auth.models import User

class StockViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'password')
        self.client.login(username='admin', password='password')
        self.stock1 = Stock.objects.create(name="Apple", symbol="AAPL", latest_price=150.00)
        self.stock2 = Stock.objects.create(name="Tesla", symbol="TSLA", latest_price=600.00)

    def test_list_stocks(self):
        response = self.client.get(reverse('stock-list'))
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_search_stocks(self):
        response = self.client.get(reverse('stock-list'), {'search': 'Tesla'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Tesla')

    def test_retrieve_stock(self):
        response = self.client.get(reverse('stock-detail', args=[self.stock1.id]))
        stock = Stock.objects.get(id=self.stock1.id)
        serializer = StockSerializer(stock)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
