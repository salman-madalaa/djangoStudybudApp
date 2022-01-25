from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    #patispants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
    
    def __str__(self):
        return self.name; 