from django.db import models
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    #host =
    #topic =
    topic = models.
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    #patispants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name,self.description; 