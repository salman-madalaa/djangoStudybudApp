from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from room.models import Room
from .serializers import RoomSerializer
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return Response(routes)  # Note: Safe is allow this list turn into a JSON List

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all();  # Note : Serializers are used to convert python objects turn into a Json objects
    return Response(rooms)
