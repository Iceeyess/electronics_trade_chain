from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """Class for overriding User"""
    email = models.EmailField(max_length=150, unique=True)

    USERNAME_FIELD = 'email'    #  remarks for log in.
    REQUIRED_FIELDS = []
