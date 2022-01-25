from django.forms import ModelForm
# from django.contrib.auth.models import User
from room
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        