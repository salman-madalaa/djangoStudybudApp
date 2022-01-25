from django.forms import ModelForm
from django.contrib.auth.models import User
from room.models import Person

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','middel_name','last_name','email','phone_mobile','is_staff','is_active']