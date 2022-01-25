from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAllRooms/',views.getAllRooms,name='room'),
    path('getroom/',views.getAllRooms,name='room')getRoomById
]