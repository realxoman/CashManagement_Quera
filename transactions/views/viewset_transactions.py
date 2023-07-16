from django.db.models import Sum, F, Q, IntegerField
from django.db.models.functions import TruncMonth
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


from transactions.models import Transaction
from transactions.serializers import TransactionSerializer, TransactionMonthlyReportSerializer
from shared import TransactionType


class TransactionViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['amount', 'date', 'type', 'category']
    filterset_fields = ['amount', 'date', 'type', 'category']

    @action(detail=False, methods=['get'], url_name="monthly-report")
    def monthly_report(self, request):
        transactions = Transaction.objects.filter(user=request.user).annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total_income=Sum('amount', filter=Q(type=TransactionType.INCOME), output_field=IntegerField(), default=0),
            total_expense=Sum('amount', filter=Q(type=TransactionType.EXPENSE), output_field=IntegerField(), default=0),
            total_amount=F('total_income') - F('total_expense')
        ).order_by('-month')
        serializer = self.get_serializer_class()(transactions, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'monthly_report':
            return TransactionMonthlyReportSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(user=user)
        return queryset
