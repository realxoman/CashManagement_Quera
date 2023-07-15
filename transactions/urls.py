from django.urls import path, include
from rest_framework import routers

from transactions.views import TransactionViewset

app_name = 'transactions'
router = routers.DefaultRouter()
router.register('', TransactionViewset, basename='transactions')

urlpatterns = [
    path('', include(router.urls))
]
