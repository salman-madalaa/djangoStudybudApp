In this project i "replace" the default User Model to Custome Model(User)

In this Project i  create User model with additional fields like image, phonenumber,...etc . The model is :

Here "AbstractUser" class is  " from django.contrib.auth.models import AbstractUser " 



class User(AbstractUser):
    middel_name = models.CharField(_('middle name'), max_length=150, blank=True)
    phone_office = models.CharField(_('phone office'), max_length=150, blank=True)
    phone_mobile = models.CharField(_('phone mobile'), max_length=150, blank=True)
    emailVerified  = models.BooleanField(_('email verified'), default=False)
    image = models.ImageField(_('image'),null=True,default="avatar.svg")
    email = models.EmailField(_('email'),unique=True,null=True)
    
    class Meta:
        db_table = 'User'  # This is use for to give name to the database table.
        swappable = 'AUTH_USER_MODEL'
        
    def __str__(self):
        return self.first_name; 




Note : In this project i replace the "from django.contrib.auth.models import User " to " from room.models import User" .
--> In settings.py file  we define the auth user model by  " AUTH_USER_MODEL = 'room.User' " . So that default auth user model is replace with custom user model.