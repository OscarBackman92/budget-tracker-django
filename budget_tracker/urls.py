from django.contrib import admin
from django.urls import path, include
from budget_tracker.views import APIRootView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),  # ✅ API Root now at `/`
    
    # ✅ Admin Panel
    path("admin/", admin.site.urls),

    # ✅ Authentication Endpoints
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),

    # ✅ Simple JWT Token Refresh (Fix Applied)
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include("transactions.urls")),
]
