from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return JsonResponse(routes,sa)
