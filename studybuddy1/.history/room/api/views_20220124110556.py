from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return JsonResponse(routes,safe=False)  # Note: Safe is allow this list turn into a JSON List