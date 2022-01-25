from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllRooms),
    path('getAllRooms/',views.getAllRooms,name='Get All Rooms'),
    path('getRoom/<str:id>/',views.getRoomById,name='Get Room By Id'),
    path('create/',views.createRoom,name='create-room'),
    path('update/<str:id>/',views.updateRoom,name='update-room'),
    path('delete/<str:id>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:id>/',views.deleteMessage,name='delete-message'),
    #
    path('topics/',views.topicsPage,name='topics'),
]