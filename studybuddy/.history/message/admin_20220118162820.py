from django.contrib import admin
from .models import 
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display =['id','name','description','created','updated'];

admin.site.register(Message,MessageAdmin)