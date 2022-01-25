from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def Home(request):
    return HttpResponse("This is Home Page")


def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
           
            user = authenticate(request, username=username, password=password)  # This is authenticate method proded by django we can pass the username and password then it return user object
            if user is not None:
                login(request, user)
                return redirect('Get All Rooms')
            else:
                messages.error(request, 'password is incorrect ')
        except:
            messages.error(request, 'username does not exist')

    context = {}
    return render(request, 'room/login_register.html', context)

def logoutUser(request):
    ret
