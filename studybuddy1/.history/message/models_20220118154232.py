from django.db import models
from room.models import Room
# Create your models here.
# Each Room has a  message   " one to many Relationship "
class Message(models.Model):
    #user =
    room = models.ForeignKey(Room,on_)
    