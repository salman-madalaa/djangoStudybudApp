from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def Home(request):
    return HttpResponse("This is Home Page")


def Login(request):
    page = 'login';
    if request.user.is_authenticated:
        return redirect('Get All Rooms')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = {'page':page}
    return render(request, 'room/login_register.html', context)

def Logout(request):
    logout(request)
    return redirect('login')

def RegisterPage(request):
    page='Register';
    registrationform = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # here we put commit is false so it does not save in data base  and we can get the user object . Because we can change the username  to be lower case . 
            user.username = user.username.lower();
            user.save(); # then After username is converted in to lower case then we can save the user object
            login(request, user);
            return redirect('Get All Rooms');
        else:
            messages.error(request, 'An error occurred during registration')
    context= {'page':page,'registrationForm':registrationform}
    return render(request,'room/login_register.html',context)
