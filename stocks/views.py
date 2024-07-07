from rest_framework import generics, status
from rest_framework.response import Response
from .models import Stock, Transaction, Holding
from .serializers import StockSerializer, TransactionSerializer, HoldingSerializer
from rest_framework import permissions
from .permissions import IsAdmin, IsInvestor

class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

class HoldingListView(generics.ListAPIView):
    serializer_class = HoldingSerializer
    permission_classes = [IsInvestor]

    def get_queryset(self):
        return Holding.objects.filter(user=self.request.user)

class StockCreateView(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

class StockUpdateView(generics.UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

class StockDeleteView(generics.DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

class BuySellStockView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsInvestor]

    def create(self, request, *args, **kwargs):
        # Set the default user if none is provided in the request
        request.data['user'] = request.user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.data['user']
        stock = serializer.validated_data['stock']
        transaction_type = serializer.validated_data['transaction_type']
        quantity = serializer.validated_data['quantity']

        # Get or create the holding for this user and stock, initializing quantity to 0 if created
        holding, created = Holding.objects.get_or_create(user_id=user, stock=stock, defaults={'quantity': 0})

        if transaction_type == Transaction.BUY:
            holding.quantity += quantity
        elif transaction_type == Transaction.SELL:
            if holding.quantity < quantity:
                return Response({'error': 'Not enough stock to sell'}, status=status.HTTP_400_BAD_REQUEST)
            holding.quantity -= quantity

        holding.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserHoldingsListView(generics.ListAPIView):
    serializer_class = HoldingSerializer
    permission_classes = [IsInvestor]

    def get_queryset(self):
        return Holding.objects.filter(user=self.request.user)
