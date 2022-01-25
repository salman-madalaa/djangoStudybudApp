from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAll/',views.getAllRooms,name='room'),
    getRoomById
]