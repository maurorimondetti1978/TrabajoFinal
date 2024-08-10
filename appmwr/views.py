from django.shortcuts import render
from django.http import HttpResponse
from .models import Clase, Profesor

def inicio(request):
    return render(request, "appmwr/inicio.html")

def clases(request):

    clases=Clase.objects.all()

    return render(request,"appmwr/clases.html", {"clases":clases})


def alumnos(request):
    return render(request, "appmwr/alumnos.html")

def profesores(request):

    profesores=Profesor.objects.all()

    return render(request, "appmwr/profesores.html", {"profesores":profesores})
