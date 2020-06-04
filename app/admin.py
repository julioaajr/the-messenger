from django.contrib import admin
from .models import Amigos, Amizade

# Register your models here.
admin.site.register(Amizade)
admin.site.register(Amigos)