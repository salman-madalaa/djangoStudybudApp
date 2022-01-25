from django.shortcuts import render

def Message(request):
    return render(request, 'message/message.html')