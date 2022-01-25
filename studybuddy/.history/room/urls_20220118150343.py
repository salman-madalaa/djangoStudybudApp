from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAllRooms/',views.getAllRooms,name='Get All Rooms'),
    path('getRoom/',views.getRoomById,name='Get Room By id')
]