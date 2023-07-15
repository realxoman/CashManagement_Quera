from django.db import models
from django.db.models import Sum, Case, When
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

from shared import TransactionType


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    username = models.CharField(_("Username"), max_length=128, unique=True)
    balance = models.DecimalField(_("Balance"), max_digits=20, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def update_balance(self):
        balance = self.transaction_set.aggregate(
            income=Sum(
                Case(
                    When(transaction_type=TransactionType.INCOME,
                         then='amount'),
                    default=0,
                    output_field=models.DecimalField()
                )
            ),
            expense=Sum(
                Case(
                    When(transaction_type=TransactionType.EXPENSE,
                         then='amount'),
                    default=0,
                    output_field=models.DecimalField()
                )
            ),
        )

        income = balance.get('income', 0)
        expense = balance.get('expense', 0)
        self.balance = income - expense
        self.save()
