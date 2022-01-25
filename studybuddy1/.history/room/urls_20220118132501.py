from django.urls import path
from . import views

urlpatterns = [
    path('', views.Room),
    path('room/<str')
]