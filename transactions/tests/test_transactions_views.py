from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from transactions.models import Transaction
from shared import TransactionType


class TransactionViewsetTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.transaction_data = {
            'amount': 100,
            'type': TransactionType.INCOME,
            'category': 1,
            'date': '2023-07-15'
        }

    def test_create_transaction(self):
        # Test creating a new transaction
        url = reverse('transactions:transactions-list')
        response = self.client.post(url, self.transaction_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the transaction was created in the database
        transaction_count = Transaction.objects.filter(user=self.user).count()
        self.assertEqual(transaction_count, 1)

    def test_list_transactions(self):
        # Test listing transactions for the authenticated user
        Transaction.objects.create(
            amount=50,
            type=TransactionType.EXPENSE,
            category=2,
            date='2023-07-14',
            user=self.user
        )
        url = reverse('transactions:transactions-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serializer used for listing is TransactionSerializer
        self.assertEqual(response.data['results'][0]['amount'], '50.00')  # Assuming TransactionSerializer displays amount as a string

    def test_filter_transactions(self):
        # Test filtering transactions by transaction type
        Transaction.objects.create(
            amount=200,
            type=TransactionType.EXPENSE,
            category=2,
            date='2023-07-13',
            user=self.user
        )
        Transaction.objects.create(
            amount=300,
            type=TransactionType.INCOME,
            category=3,
            date='2023-07-12',
            user=self.user
        )
        url = reverse('transactions:transactions-list')
        response = self.client.get(url, {'type': TransactionType.INCOME})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_monthly_report(self):
        # Test the monthly_report action
        Transaction.objects.create(
            amount=1000,
            type=TransactionType.INCOME,
            category=1,
            date='2023-06-10',
            user=self.user
        )
        Transaction.objects.create(
            amount=500,
            type=TransactionType.EXPENSE,
            category=2,
            date='2023-06-20',
            user=self.user
        )
        Transaction.objects.create(
            amount=800,
            type=TransactionType.INCOME,
            category=3,
            date='2023-07-05',
            user=self.user
        )
        Transaction.objects.create(
            amount=200,
            type=TransactionType.EXPENSE,
            category=4,
            date='2023-07-25',
            user=self.user
        )
        url = reverse('transactions:transactions-monthly-report')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serializer used for monthly_report is TransactionMonthlyReportSerializer
        self.assertEqual(response.data[0]['total_income'], 800)
        self.assertEqual(response.data[0]['total_expense'], 200)
        self.assertEqual(response.data[0]['total_amount'], 600)
