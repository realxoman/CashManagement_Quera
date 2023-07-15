from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import permissions

from accounts.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    permissions = [permissions.IsAdminUser()]
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return self.permissions
