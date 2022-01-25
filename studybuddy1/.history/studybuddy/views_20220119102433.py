from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("This is Home Page");

def LoginPage(request):
    
    if request.method == 'POST':
        usernames = request.POST.get('username');
        password = request.POST.get('password');
        
        try:
            user = 
    
    context = {}
    return render(request, 'room/login_register.html', context)