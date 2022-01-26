from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Topic(models.Model):
    name = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name;

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name="participants",blank=True)  # many to many relationship   Note: Here related_name is use for already we use User in the above field (host) so we differenciate both using related_name 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = [
            '-id','-updated',
        ]
    
    def __str__(self):
        return self.name; 
    

