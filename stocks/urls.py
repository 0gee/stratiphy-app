from django.urls import path
from .views import StockListView, StockDetailView, BuySellStockView, TransactionListView, HoldingListView

urlpatterns = [
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
    path('stocks/buy-sell/', BuySellStockView.as_view(), name='buy-sell-stock'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('holdings/', HoldingListView.as_view(), name='holding-list'),
]
