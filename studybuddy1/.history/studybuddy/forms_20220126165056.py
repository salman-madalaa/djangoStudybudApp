from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from room.models import User

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','email']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','middel_name','last_name','username','password','email','phone_mobile','image','is_active']