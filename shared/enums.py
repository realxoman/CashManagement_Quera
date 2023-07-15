from django.db import models


class TransactionType(models.IntegerChoices):
    INCOME = 1, "Income"
    EXPENSE = 2, "Expense"


class TransactionCategory(models.IntegerChoices):
    GROCERIES = 1, "Groceries"
    UTILITIES = 2, "Utilities"
    ENTERTAINMENT = 3, "Entertainment"
    OTHER = 4, "Other"
