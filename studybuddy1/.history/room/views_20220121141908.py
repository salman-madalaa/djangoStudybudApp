from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from message.models import Message
# Create your views here.

# Note: Here we are using the login_required method it always check wether user is login or not  . if user not login then it directly go to the login page .

# ----------------get all Method -------------------
@login_required(login_url='/user/login')
def getAllRooms(request):
    q = request.GET.get('q') if request.GET.get('q') != None else '' # This line is used for get filter value getting from browser.
    rooms = Room.objects.filter(   # Throoug the filter value filter the filtered room objects .
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    topics = Topic.objects.all()  # getting the all topic objects from database
    room_count = rooms.count()  # here we can directly get the count by using count() method .
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = q))  # This is for getting the messages based on the filter value .
    
    context = {'rooms': rooms,'topics': topics,'room_count':room_count,'room_messages':room_messages}
    return render(request, 'room/allRooms.html', context)



# ----------------Get Room By id Method -------------------
@login_required(login_url='/user/login')
def getRoomById(request, id):
    room = Room.objects.get(id=int(id));
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all();
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('Get Room By Id',id=room.id)
    
    context = {'room': room,'room_messages':room_messages,'participants':participants}
    return render(request, 'room/roomDetails.html', context)



# ----------------create Method -------------------
@login_required(login_url='/user/login')
def createRoom(request):
    type="Create"
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False) # So that it give an instance to that form 
            room.host 
            # here " Get All Room " is the name of the url which is present in the urls.py file
            return redirect('Get All Rooms')
    context = {'form': form,'type':type}
    return render(request, 'room/room_form.html', context)



# ----------------update Method -------------------
@login_required(login_url='/user/login')
def updateRoom(request, id):
    type="Update"
    room = Room.objects.get(id=int(id))
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse("You don't have permission to update this room")
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('Get All Rooms');
    context = {'form': form,'type':type}
    return render(request, 'room/room_form.html', context)



# ----------------Delete  Room Method -------------------
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



# ----------------Delete Message Method -------------------
@login_required(login_url='/user/login')
def deleteMessage(request, id):
    message = Message.objects.get(id=int(id))
    
    if request.user != message.user:
        return HttpResponse("You don't have permission to delete this message")
    
    if request.method == 'POST':
        message.delete()
        return redirect('Get All Rooms');
    context = {'obj': message}
    return render(request, 'room/deleteRoom.html', context)
    

