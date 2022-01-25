from django.db import models
from room.models import Room
# Create your models here.
# Each Room has a  message   " one to many Relationship ( one room many messages )"
class Message(models.Model):
    #user =
    room = models.ForeignKey(Room,on_delete=models.CASCADE);
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
    