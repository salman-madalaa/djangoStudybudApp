from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Room(request):
    return HttpResponse("<h1>This is Room</h1>")
def room(request):
    rooms = Room.objects.all()
    return render()