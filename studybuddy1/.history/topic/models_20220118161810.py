from django.db import models
from room.models import Room
# Create your models here.
class Topic(models.Model):
    name = models.TextField(max_length=255)
    
    def __str__(self):
        return 
    
    
   