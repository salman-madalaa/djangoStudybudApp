from django.forms import ModelForm
from django.contrib.auth.models import User
from room.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'