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
    path('leerProfesores', leerProfesores, name= "LeerProfesores"), 
    path('eliminarProfesor/<profesor_nombre>', eliminarProfesores, name= "EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>', editarProfesor, name= "EditarProfesor"), 
    path('leerClases', leerClases, name= "LeerClases"), 
    path('eliminarClases/<clases_nivel>', eliminarClases, name= "EliminarClases"),
    path('editarClases/<clases_nivel>', editarClases, name= "EditarClases"), 
    path('leerAlumnos', leerAlumnos, name= "LeerAlumnos"), 
    path('eliminarAlumno/<alumno_nombre>', eliminarAlumnos, name= "EliminarAlumno"),
    path('editarAlumno/<alumno_nombre>', editarAlumnos, name= "EditarAlumno"), 
    path('busquedaNivel', busquedaNivel, name= "busquedaNivel"),
    path('buscar/', buscar),
    path('login', login_request, name="Login"),  
    path('register', register, name="Register"),
    path('logout', LogoutView.as_view(template_name='appmwr/logout.html'), name = 'Logout'),
    path('cambiarcontrasenia', CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    path('editarPerfil', editarPerfil, name="EditarPerfil"),

]