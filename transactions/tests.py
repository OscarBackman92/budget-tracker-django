from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Transaction


class TransactionAPITestCase(APITestCase):
    """Tests for the Transactions API"""

    def setUp(self):
        """Ensure each test starts with a clean state"""
        self.client.force_authenticate(user=self.create_test_users())

        # ✅ Ensure a clean test database
        Transaction.objects.all().delete()

        # ✅ Recreate only the expected transactions
        self.transaction1 = Transaction.objects.create(
            user=self.user, title="Groceries", amount=50.00, transaction_type="expense", category="Food"
        )
        self.transaction2 = Transaction.objects.create(
            user=self.user, title="Salary", amount=5000.00, transaction_type="income", category="Work"
        )

    def create_test_users(self):
        """Create users once per test class to avoid duplication"""
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpass")
        return self.user

    def test_user_can_register(self):
        """Ensure a new user can register successfully"""
        data = {"username": "newuser", "password1": "securepassword", "password2": "securepassword"}
        response = self.client.post("/auth/registration/", data)

        print("🔍 DEBUG: User Registration Response:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # ✅ Accept either JWT (`access`) or default `auth_token` (`key`)
        self.assertTrue("access" in response.data or "key" in response.data)

    def test_user_can_login(self):
        """Ensure a user can log in and receive a token"""
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post("/auth/login/", data)

        print("🔍 DEBUG: User Login Response:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data or "key" in response.data)

    def test_create_transaction(self):
        """Ensure an authenticated user can create a transaction"""
        data = {
            "title": "Freelance Payment",
            "amount": 1000.00,
            "transaction_type": "income",
            "category": "Work",
            "description": "Freelance job payment"
        }
        response = self.client.post("/transactions/", data)

        print("🔍 DEBUG: Transaction Create Response:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.filter(user=self.user).count(), 3)  # 2 from setup + 1 new

    def test_get_transactions(self):
        """Ensure an authenticated user can fetch only their own transactions"""
        response = self.client.get("/transactions/")

        print("🔍 DEBUG: Transactions Retrieved:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # ✅ Check the number of transactions inside "results"
        self.assertEqual(len(response.data["results"]), 2)  # User should only see their own transactions

    def test_user_cannot_access_transactions_without_authentication(self):
        """Ensure unauthenticated users cannot access transactions"""
        self.client.logout()
        response = self.client.get("/transactions/")

        print("🔍 DEBUG: Unauthorized Transactions Request:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_transaction(self):
        """Ensure a user can update their own transaction"""
        data = {"amount": 75.00}
        response = self.client.patch(f"/transactions/{self.transaction1.id}/", data)

        print("🔍 DEBUG: Transaction Update Response:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.transaction1.refresh_from_db()
        self.assertEqual(self.transaction1.amount, 75.00)

    def test_delete_transaction(self):
        """Ensure a user can delete their own transaction"""
        response = self.client.delete(f"/transactions/{self.transaction1.id}/")

        print("🔍 DEBUG: Transaction Delete Response Status:", response.status_code)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Transaction.objects.filter(id=self.transaction1.id).exists())

    def test_user_cannot_delete_another_users_transaction(self):
        """Ensure a user cannot delete another user's transaction"""
        other_transaction = Transaction.objects.create(
            user=self.other_user, title="Coffee", amount=5.00, transaction_type="expense", category="Food"
        )

        response = self.client.delete(f"/transactions/{other_transaction.id}/")

        print("🔍 DEBUG: Unauthorized Delete Response:", response.data)  # ✅ Debugging print

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  # Should not find another user's transaction
