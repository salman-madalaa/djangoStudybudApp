from django.forms import ModelForm
# from django.contrib.auth.models import User
from room.models import Person
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        