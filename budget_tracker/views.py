from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

class APIRootView(APIView):
    """
    API Root that dynamically lists all available API endpoints.
    """
    permission_classes = [AllowAny]  # ✅ Allow public access

    def get(self, request, format=None):
        return Response({
            "Admin Panel": request.build_absolute_uri(reverse("admin:index")),
            "Authentication": {
                "Login": request.build_absolute_uri(reverse("rest_login")),
                "Logout": request.build_absolute_uri(reverse("rest_logout")),
                "Register": request.build_absolute_uri(reverse("rest_register")),
                "Token Refresh": request.build_absolute_uri("/auth/token/refresh/"),  # ✅ Change to hardcoded URL
            },
            "Transactions": {
                "List": request.build_absolute_uri(reverse("transaction-list")),
                "Create": request.build_absolute_uri(reverse("transaction-list")),
                "Retrieve/Update/Delete": request.build_absolute_uri("/transactions/{id}/"),
            },
        })
