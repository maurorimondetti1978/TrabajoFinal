from django.urls import path
from appmwr.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clases", clases, name="clases"),
    path("alumnos", alumnos, name= "alumnos"),
    path("profesores", profesores, name= "profesores"),
    path('alumnoFormulario', alumnoFormulario, name= "alumnoformulario"), 
    path('claseFormulario', claseFormulario, name= "claseformulario"), 
    path('profesorFormulario', profesorFormulario, name= "profesorformulario"), 
    path('busquedaNivel', busquedaNivel, name= "busquedaNivel"),
    path('buscar/', buscar),
    path('login', login_request, name="Login"),  
    path('register', register, name="Register"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = 'Logout'),
    path('editarperfil', editarPerfil, name="EditarPerfil"),
    path('cambiarcontrasenia', CambiarContrasenia.as_view(), name="CambiarContrasenia"),
]