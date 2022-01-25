from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .templates import rooms
# Create your views here.

def RoomHome(request):
    return HttpResponse("<h1>This is Room</h1>")

def getAllRooms(request):
    rooms = Room.objects.all().order_by('-id');
    context = {'rooms':rooms}
    return render(request, 'room/home.html',context)

def getRoomById(request,id):
    rooms = Room.objects.get(id=int(id));
    context = {'rooms':rooms}
    return render(request, 'room/room.html',context)