from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import permissions

from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer, UserBalanceSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    permissions = [permissions.IsAdminUser()]
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    @action(detail=False, methods=['get'])
    def balance(self, request):
        user = self.request.user
        serializer = self.get_serializer_class()(user)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'balance':
            return UserBalanceSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action == 'balance':
            return [permissions.IsAuthenticated()]
        return self.permissions
