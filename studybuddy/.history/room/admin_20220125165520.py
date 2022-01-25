from django.contrib import admin
from .models import Room, Topic,Person
# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id','host','topic', 'name', 'description', 'created', 'updated'] 

class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Room,RoomAdmin)
admin.site.register(Topic,TopicAdmin)
# admin.site.register(Person)