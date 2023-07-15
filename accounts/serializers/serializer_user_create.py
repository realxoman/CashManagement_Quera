from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)

    def validate_username(self, value):
        """
            This function checks that the username does not exist in the database
        """
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError(
                _("The user exists with this username."))
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        return user
