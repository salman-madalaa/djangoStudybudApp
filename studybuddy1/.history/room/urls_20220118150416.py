from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAllRooms/',views.getAllRooms,name='Get All Rooms'),
    path('getRoom/<str:id>/',views.getRoomById,name='Get Room By Id')
]