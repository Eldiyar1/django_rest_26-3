from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserAuthorizeSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreatSerializer(UserAuthorizeSerializer): # Тут мы наследуесмя от
                                                    # UserAuthorizeSerializer

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User is already exists!')
