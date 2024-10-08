import uuid
from datetime import datetime
from datetime import timedelta

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)

    def generate_auth_token(self, expiration=3600):
        expires = timezone.now() + timedelta(seconds=expiration)
        token = Token.objects.create(user=self, value=uuid.uuid4(), expires=expires)
        return token


# Foreign key: 1:M
#  many to many: M:M
#  One to one : 1:1
#  many to one : M:1


class Token(models.Model):
    value = models.CharField(max_length=255)
    expires = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_valid(self):
        return self.expires < timezone.now() and self.is_active
