from django.contrib import admin
from .m
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display =['id','name','description','created','updated'];

admin.site.register(Message,MessageAdmin)