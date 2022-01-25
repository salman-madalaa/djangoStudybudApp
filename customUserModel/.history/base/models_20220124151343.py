from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(unique=True max_length=255,null=True)
    pass