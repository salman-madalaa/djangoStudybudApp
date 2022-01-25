from django.contrib import admin
from .models import Room
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display =['id','name','dob','marks','email','phoneNumber','address'];

admin.site.register(Room)