from django.urls import path
from . import views

urlpatterns = [
    path('', views.Room),
    path('getAll/',views.getAllRooms,name='room')
]