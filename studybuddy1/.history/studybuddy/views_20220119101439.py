from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("This is Home Page");

def Login(request):
    context = {}
    return render(request, 'room/login_register.html', context)