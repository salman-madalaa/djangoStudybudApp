from django.contrib import admin
from .models import Room,Topic
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display =['id','name','description','created','updated'];

admin.site.register(Room,RoomAdmin)
admin.site.register(admin.site.register(Room,RoomAdmin)
,RoomAdmin)