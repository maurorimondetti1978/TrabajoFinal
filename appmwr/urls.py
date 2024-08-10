from django.urls import path
from appmwr.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clases", clases, name="clases"),
    path("alumnos", alumnos, name= "alumnos"),
    path("profesores", profesores, name= "profesores"),

    
]