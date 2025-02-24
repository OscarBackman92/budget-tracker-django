from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # ✅ Only return transactions for the logged-in user
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # ✅ Assign the logged-in user when creating a new transaction
        serializer.save(user=self.request.user)
