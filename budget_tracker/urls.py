from django.contrib import admin
from django.urls import path, include
from budget_tracker.views import home_view  # ✅ Import from budget_tracker.views

urlpatterns = [
    path("", home_view, name="home"),  # ✅ Default homepage
    path("admin/", admin.site.urls),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
]
