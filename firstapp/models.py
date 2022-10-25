from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User custom model"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    organization_role = models.CharField(max_length=20, default="Associate")
    is_active = models.BooleanField(default=True)
    avatar = models.CharField(max_length=250, blank=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def hidden_name(self):
        name = self.first_name + " " + self.last_name
        return name.replace(name[3:-3], "*"*(len(name)-6))

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
