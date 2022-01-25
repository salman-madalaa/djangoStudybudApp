from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.

def RoomHome(request):
    return HttpResponse("<h1>This is Room</h1>")

def getAllRooms(request):
    rooms = Room.objects.all().order_by('-id');
    context = {'rooms':rooms}
    return render(request, 'room/allRooms.html',context)

def getRoomById(request,id):
    room = Room.objects.get(id=int(id));
    context = {'room':room}
    return render(request, 'room/roomDetails.html',context)

def createRoom(request):
    return render(request, 'room/room_')