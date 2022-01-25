from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Message(request):
    return HttpResponse("This is Message page")