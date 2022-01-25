from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAllRooms/',views.getAllRooms,name='room'),
    path('getRoom/',views.getAllRooms,name='room')
]