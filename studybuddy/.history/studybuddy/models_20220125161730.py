from django.db import models

class User(models.Model):
    middel_name = models.CharField(_('middle name'), max_length=150, blank=True)
    phone_office = models