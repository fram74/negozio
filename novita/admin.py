from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Novita

class NovitaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Novita, NovitaAdmin)