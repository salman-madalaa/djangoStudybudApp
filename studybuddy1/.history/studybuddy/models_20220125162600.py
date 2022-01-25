from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Person(models.Model):
    middel_name = models.CharField(_('middle name'), max_length=150, blank=True)
    phone_office = models.CharField(_('phone office'), max_length=150, blank=True)
    phone_mobile = models.CharField(_('phone mobile'), max_length=150, blank=True)
    emailVerified  = models.BooleanField(_('email verified'), default=False)
    image = models.ImageField(_('image'),null=True,default="avatar.svg")
    user = models.OneToOneField(_('user'),User,related_name="participants",blank=True)