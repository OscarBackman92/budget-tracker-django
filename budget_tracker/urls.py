from django.contrib import admin
from django.urls import path, include
from budget_tracker.views import APIRootView
from rest_framework_simplejwt.views import TokenRefreshView  # ✅ Correct Import

urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),  # ✅ API Root now at `/`
    
    # ✅ Admin Panel
    path("admin/", admin.site.urls),

    # ✅ Authentication Endpoints
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),

    # ✅ Simple JWT Token Refresh (Fix Applied)
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ✅ Transactions API
    path("", include("transactions.urls")),
]
