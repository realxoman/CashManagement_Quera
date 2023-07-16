from django.test import TestCase

from accounts.models import CustomUser
from shared import TransactionType
from transactions.models import Transaction


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_create_user(self):
        # Check if the user is created successfully
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.balance, 0)

    def test_update_balance(self):
        Transaction.objects.create(user=self.user, amount=100, type=TransactionType.INCOME)
        Transaction.objects.create(user=self.user, amount=50, type=TransactionType.EXPENSE)

        # Update the balance
        self.user.update_balance()

        # Check if the balance is updated correctly
        self.assertEqual(self.user.balance, 50)

    def test_update_balance_no_transactions(self):
        # Test the balance update when there are no transactions
        self.user.update_balance()
        self.assertEqual(self.user.balance, 0)

    def test_update_balance_income_only(self):
        # Test the balance update when there are only income transactions
        Transaction.objects.create(user=self.user, amount=200, type=TransactionType.INCOME)
        self.user.update_balance()
        self.assertEqual(self.user.balance, 200)

    def test_update_balance_expense_only(self):
        # Test the balance update when there are only expense transactions
        Transaction.objects.create(user=self.user, amount=75, type=TransactionType.EXPENSE)
        self.user.update_balance()
        self.assertEqual(self.user.balance, -75)
