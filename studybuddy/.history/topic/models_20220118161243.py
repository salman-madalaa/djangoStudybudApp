from django.db import models
from room.models import Room
# Create your models here.
class Topic(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE);
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
   