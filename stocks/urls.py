# stocks/urls.py

from django.urls import path
from .views import StockListView, StockDetailView

urlpatterns = [
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
]
