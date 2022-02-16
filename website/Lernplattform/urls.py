"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import django.contrib.auth.views
from . import views

app_name = 'Lernplattform'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # path('login/', django.contrib.auth.views.LoginView.as_view(), {'template_name' : 'login.html'}, name='login'),
    path('fragebogen/', views.fragebogen, name='fragebogen'),
    path('fragebogen/details/<int:pk>',
         views.fragebogenDetails, name='fragebogenDetails'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
