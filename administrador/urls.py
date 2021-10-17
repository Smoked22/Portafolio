from os import name
from django.contrib import admin
from django.urls import path
from .views import home, normal, acceder
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
   #url(r'^$', administrador_views.iniciar_sesion, name='index'),
   url(r'^normal/$', normal),
   path('home/', home, name="home"),
   path('', acceder, name="inicio"),
]
