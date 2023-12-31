from django.contrib import admin

from transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("type", "category", "user", "amount", "date")
