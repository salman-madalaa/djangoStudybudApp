from django.shortcuts import render
from django.http import HttpResponse

def Message(request):
    return render(request, '/message/message.html')