from django.db.models import fields
from rest_framework import serializers

# https://djoser.readthedocs.io/en/latest/settings.html#serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'password', "first_name", "last_name", "avatar")


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('email', "first_name", "last_name", "avatar")
        ref_name = "UserSerializer"