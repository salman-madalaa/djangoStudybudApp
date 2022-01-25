from django.contrib import admin
from .models import Room
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =['rollNo','name','dob','marks','email','phoneNumber','address'];

admin.site.register(Room)