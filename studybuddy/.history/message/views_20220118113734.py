from django.shortcuts import render
from django.http import HttpResponse

def Message(request):
    return HttpResponse("<h1>This is Message page</h1>")