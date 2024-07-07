from django.urls import path
from .views import *
urlpatterns = [
    path('stocks/', StockListView.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
    path('stocks/buy-sell/', BuySellStockView.as_view(), name='buy-sell-stock'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('holdings/', HoldingListView.as_view(), name='holding-list'),
    path('user/holdings/', UserHoldingsListView.as_view(), name='user-holdings'),
    path('stocks/create/', StockCreateView.as_view(), name='stock-create'),
    path('stocks/update/<int:pk>/', StockUpdateView.as_view(), name='stock-update'),
    path('stocks/delete/<int:pk>/', StockDeleteView.as_view(), name='stock-delete'),
]

