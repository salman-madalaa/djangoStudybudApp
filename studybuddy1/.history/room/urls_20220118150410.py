from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomHome),
    path('getAllRooms/',views.getAllRooms,name='Get All Rooms'),
    path('getRoom/<str',views.getRoomById,name='Get Room By Id')
]