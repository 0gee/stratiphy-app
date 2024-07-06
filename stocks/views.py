# stocks/views.py

from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Stock
from .serializers import StockSerializer

class StockFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = ['name']

class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StockFilter

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
