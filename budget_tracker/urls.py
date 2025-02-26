from django.contrib import admin
from django.urls import path, include
from budget_tracker.views import APIRootView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),  # ✅ API Root now at `/`
    path("admin/", admin.site.urls),
    path("auth/", include("dj_rest_auth.urls")),  # ✅ Includes login, logout, password reset, etc.
    path("auth/registration/", include("dj_rest_auth.registration.urls")),  # ✅ Enables registration
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # ✅ Add JWT login endpoint
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("transactions/", include("transactions.urls")),
]
