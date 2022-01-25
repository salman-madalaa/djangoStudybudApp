from django.db import models

class User(models.Model):
    middel_name = models.CharField(_('last name'), max_length=150, blank=True)