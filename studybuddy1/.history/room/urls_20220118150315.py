from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAllroom/',views.getAllRooms,name='room'),
    path('getroom/',views.getAllRooms,name='room')getRoomById
]