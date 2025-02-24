from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API View for managing transactions.
    Users can create, view, update, and delete their transactions.
    """
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    # ✅ Filter transactions for the authenticated user
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by("-date")

    # ✅ Automatically assign the user when creating a transaction
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # ✅ Enable filtering by category and date
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ["transaction_type", "category"]
    search_fields = ["title", "description"]
    ordering_fields = ["amount", "date"]
