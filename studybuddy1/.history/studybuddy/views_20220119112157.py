from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def Home(request):
    return HttpResponse("This is Home Page");

def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username');
        password = request.POST.get('password');
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'user does not exist')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)

    
    context = {}
    return render(request, 'room/login_register.html', context)