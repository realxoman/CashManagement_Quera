from django.db import models
from django.db.models import Sum, Q
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

from shared import TransactionType


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    username = models.CharField(_("Username"), max_length=128, unique=True)
    balance = models.IntegerField(_("Balance"), default=0)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def update_balance(self):
        balance = self.transaction_set.aggregate(
            income=Sum(
                    'amount',
                    filter=Q(type=TransactionType.INCOME),
                    default=0,
                    output_field=models.IntegerField()
            ),
            expense=Sum(
                    'amount',
                    filter=Q(type=TransactionType.EXPENSE),
                    default=0,
                    output_field=models.IntegerField()
            ),
        )

        income = balance.get('income', 0)
        expense = balance.get('expense', 0)
        self.balance = income - expense
        self.save()
