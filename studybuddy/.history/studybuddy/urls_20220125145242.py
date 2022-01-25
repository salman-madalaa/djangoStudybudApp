"""studybuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from studybuddy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='Home'),
    path('room/',include('room.urls')),
    path('message/',include('message.urls')),
    
    path('api/',include('room.api.urls')),
    
    # login
    path('user/login/', views.Login, name="login"),
    # logout
    path('user/logout/', views.Logout, name="logout"),
    # Register
    path('user/register/', views.RegisterPage, name="register"),
    
    path('profile/<str:id>/', views.UserProfile, name="user-profile"),
    
    # update User
    path('user/update/', views.updateUser, name="update-user"),
    
]

ur
