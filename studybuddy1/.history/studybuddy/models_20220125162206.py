from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    middel_name = models.CharField(_('middle name'), max_length=150, blank=True)
    phone_office = models.CharField(_('phone office'), max_length=150, blank=True)
    phone_mobile = models.CharField(_('phone mobile'), max_length=150, blank=True)
    emailVerified  = models.BooleanField(_('email verified'), default=False)
    image = models.ImageField(_('image'),)