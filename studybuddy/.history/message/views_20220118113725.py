from django.shortcuts import render
from django.http import HttpResponse

def Message(request):
    return HttpResponse("h1This is Message page")