from django.forms import ModelForm
from .models import Room
from django.conf import settings

User = settings.AUTH_USER_MODEL

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' 
        exclude = ['host','participants']

        