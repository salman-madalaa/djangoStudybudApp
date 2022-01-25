from django.db import models

# Create your models here.
# Each Room has a multiple message one to many Relationship
class Message(models.Model):
    