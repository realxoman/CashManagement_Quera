from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
        read_only_field = ('id', )
