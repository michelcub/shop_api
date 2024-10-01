from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

import uuid

# Create your models here.
class User(AbstractUser):
    key = models.URLField(default=uuid.uuid4,  primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=80)
    email = models.EmailField(max_length=80, unique=True)
    password = models.CharField(max_length=80)
    avatar = models.URLField(blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']



