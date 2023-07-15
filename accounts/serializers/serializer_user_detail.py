from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'is_active', 'is_staff')
        read_only_field = ('id', )
