from django.shortcuts import render

# Create your views here.

def Room(request):
    return HttpResponse("<h1>This is room</h1>")