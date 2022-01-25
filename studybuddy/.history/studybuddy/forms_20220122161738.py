from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = ['username',''],
        fields = '__all__',
        