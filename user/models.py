import uuid

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=80, unique=True)
    avatar = models.URLField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]
