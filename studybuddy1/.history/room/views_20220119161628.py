from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from message.models
# Create your views here.

# Note: Here we are using the login_required method it always check wether user is login or not  . if user not login then it directly go to the login page .

# ----------------get all Method -------------------
@login_required(login_url='/user/login')
def getAllRooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    topics = Topic.objects.all()
    
    room_count = rooms.count()
    
    
    context = {'rooms': rooms,'topics': topics,'room_count':room_count}
    return render(request, 'room/allRooms.html', context)

# ----------------Get Room By id Method -------------------
@login_required(login_url='/user/login')
def getRoomById(request, id):
    room = Room.objects.get(id=int(id));
    messages = M
    context = {'room': room}
    return render(request, 'room/roomDetails.html', context)

# ----------------create Method -------------------
@login_required(login_url='/user/login')
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

# ----------------update Method -------------------
@login_required(login_url='/user/login')
def updateRoom(request, id):
    room = Room.objects.get(id=int(id))
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse("You don't have permission to update this room")
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('Get All Rooms');
    context = {'form': form}
    return render(request, 'room/room_form.html', context)

# ----------------Delete Method -------------------
@login_required(login_url='/user/login')
def deleteRoom(request, id):
    room = Room.objects.get(id=int(id))
    
    if request.user != room.host:
        return HttpResponse("You don't have permission to delete this room")
    
    if request.method == 'POST':
        room.delete()
        return redirect('Get All Rooms');
    context = {'obj': room}
    return render(request, 'room/deleteRoom.html', context)

