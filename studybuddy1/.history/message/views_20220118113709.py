from django.shortcuts import render
from django.http import HttpResponse

def Message(request):
    return HttpResponse("This is Message page")