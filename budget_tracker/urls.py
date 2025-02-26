from django.contrib import admin
from django.urls import path, include
from budget_tracker.views import APIRootView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from transactions.views import TransactionViewSet

# ✅ Register Transactions ViewSet
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename="transaction")

urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),  # ✅ API Root at `/`
    path("admin/", admin.site.urls),
    
    # ✅ Authentication Endpoints
    path("auth/", include("dj_rest_auth.urls")),  
    path("auth/registration/", include("dj_rest_auth.registration.urls")),  
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ✅ Fix Transactions API URL
    path("api/", include(router.urls)),  # ✅ Ensures transactions are at `/api/transactions/`
]
