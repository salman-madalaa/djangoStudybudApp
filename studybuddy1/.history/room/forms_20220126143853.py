from django.forms import ModelForm
from .models import Room
from django.conf import settings

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' 
        exclude = ['host','participants']

        