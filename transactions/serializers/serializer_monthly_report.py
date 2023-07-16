from rest_framework import serializers

from transactions.models import Transaction


class TransactionMonthlyReportSerializer(serializers.ModelSerializer):
    month = serializers.CharField()
    total_income = serializers.IntegerField()
    total_expense = serializers.IntegerField()
    total_amount = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = ('month', 'total_income', 'total_expense', 'total_amount')
