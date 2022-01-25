from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm
from d
# Create your views here.


def getAllRooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__icontains = q,name__icontains=)
    topics = Topic.objects.all()
    context = {'rooms': rooms,'topics': topics}
    return render(request, 'room/allRooms.html', context)


def getRoomById(request, id):
    room = Room.objects.get(id=int(id))
    context = {'room': room}
    return render(request, 'room/roomDetails.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            # here " Get All Room " is the name of the url which is present in the urls.py file
            return redirect('Get All Rooms')
    context = {'form': form}
    return render(request, 'room/room_form.html', context)


def updateRoom(request, id):
    room = Room.objects.get(id=int(id))
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('Get All Rooms');
    context = {'form': form}
    return render(request, 'room/room_form.html', context)

def deleteRoom(request, id):
    room = Room.objects.get(id=int(id))
    if request.method == 'POST':
        room.delete()
        return redirect('Get All Rooms');
    context = {'obj': room}
    return render(request, 'room/deleteRoom.html', context)