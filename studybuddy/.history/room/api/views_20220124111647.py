from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return JsonResponse(routes,safe=False)  # Note: Safe is allow this list turn into a JSON List
