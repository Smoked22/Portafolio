from django.contrib import admin
from django.contrib.admin.decorators import register

from administrador.views import normal
from .models import Cliente, Usuario, Menu



admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Menu)
