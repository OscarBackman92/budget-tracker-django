from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transactions.views import TransactionViewSet

# ✅ Use a router for transaction API
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path("", include(router.urls)),  # ✅ Only include transaction endpoints
]
