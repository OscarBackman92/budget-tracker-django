from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Transaction

class TransactionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

    def test_create_transaction(self):
        response = self.client.post("/api/transactions/", {
            "title": "Bonus",
            "amount": "1000.00",
            "transaction_type": "income",
            "category": "Work"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
