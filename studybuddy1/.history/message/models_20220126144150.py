from django.db import models
from room.models import Room
from room.models import User 
# Create your models here.

# Each Room has a  message   " one to many Relationship ( one room many messages )  and here user is also one to many relationship (one user has many messages )"
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE);
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = [
            '-updated','-created',
        ]
    
    def __str__(self):
        return self.body;
    