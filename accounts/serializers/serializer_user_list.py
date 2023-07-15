from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = get_user_model()
        fields = ('id', 'full_name', 'first_name', 'last_name', 'username', 'email')
        read_only_field = ('id', )
