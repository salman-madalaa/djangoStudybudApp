from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.


def getAllRooms(request):
    rooms = Room.objects.all();
    context = {'rooms':rooms}
    return render(request, 'room/allRooms.html',context)

def getRoomById(request,id):
    room = Room.objects.get(id=int(id));
    context = {'room':room}
    return render(request, 'room/roomDetails.html',context)

def createRoom(request):
    form = RoomForm();
    if request.method == 'POST':
        form = RoomForm(request.POST);
        if form.is_valid():
            form.save();
            return redirect('Get All Rooms') # here " Get All Room " is the name of the url which is present in the urls.py file 
    context = {'form':form}
    return render(request, 'room/room_form.html',context)

def updateRoom(request,id):
    room = Room.objects.get(id=int(id)); 
    form = RoomForm(instance=room)
    context = {'room':room}
    return render(request, 'room/room_form.html',context)