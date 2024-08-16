from django.contrib import admin
from .models import *
# Register your models here.

class ClaseAdmin(admin.ModelAdmin):
    list_display= ("nivel", "dias")
    list_per_page = 2
    list_filter = ("nivel", "dias")
    ordering= ("nivel", "dias")

class ProfesorAdmin(admin.ModelAdmin):
    list_display= ("nombre", "apellido", "nivel")
    list_per_page = 2
    list_filter = ("nombre", "apellido", "nivel")
    ordering= ("nombre", "apellido", "nivel")



admin.site.register(Clase, ClaseAdmin)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Avatar)
