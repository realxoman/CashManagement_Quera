from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from transactions.models import Transaction
from shared import TransactionType, TransactionCategory


class TransactionModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test transaction for the user
        self.transaction = Transaction(
            amount=100,
            type=TransactionType.INCOME,
            category=TransactionCategory.OTHER,
            date=timezone.now(),
            user=self.user
        )

    def test_transaction_create(self):
        self.transaction.save()
        self.assertEqual(self.transaction.amount, 100)

    def test_transaction_save(self):
        # Test the save method to ensure user balance is updated
        initial_balance = self.user.balance
        self.transaction.save()
        updated_user = get_user_model().objects.get(pk=self.user.pk)
        self.assertNotEqual(initial_balance, updated_user.balance)

    def test_transaction_delete(self):
        # Test the delete method to ensure user balance is updated
        initial_balance = self.user.balance
        self.transaction.save()
        self.transaction.delete()
        updated_user = get_user_model().objects.get(pk=self.user.pk)
        self.assertNotEqual(initial_balance, updated_user.balance)
