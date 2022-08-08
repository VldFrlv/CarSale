from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """User model with additional fields"""
    name = models.CharField('Name', max_length=100, unique=True)
    phone = models.CharField('Phone', max_length=15)

    def __str__(self):
        return self.username


