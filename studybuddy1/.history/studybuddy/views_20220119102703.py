from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from 
def Home(request):
    return HttpResponse("This is Home Page");

def LoginPage(request):
    
    if request.method == 'POST':
        usernames = request.POST.get('username');
        password = request.POST.get('password');
        
        try:
            user = User.objects.get(username=usernames)
        except:
            
    
    context = {}
    return render(request, 'room/login_register.html', context)