from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from shared import BaseModel, TransactionType, TransactionCategory


class Transaction(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=TransactionType.choices, default=TransactionType.EXPENSE)
    category = models.IntegerField(choices=TransactionCategory.choices, default=TransactionCategory.OTHER)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.update_balance()

    def delete(self, *args, **kwargs):
        self.user.update_balance()
        super().delete(*args, **kwargs)
