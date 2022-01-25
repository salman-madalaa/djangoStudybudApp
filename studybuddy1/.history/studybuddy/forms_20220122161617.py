from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User

Class UserForm(ModelForm):
    class Meta:
        model = User