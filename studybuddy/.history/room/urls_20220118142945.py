from django.urls import path
from . import views

urlpatterns = [
    path('', views.Room),
    path('get/',views.room,name='room')
]