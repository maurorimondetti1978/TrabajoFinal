from django.shortcuts import render
from django.http import HttpResponse
from .models import Clase, Profesor, Alumno
from .forms import AlumnoFormulario, ClaseFormulario, ProfesorFormulario

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

def claseFormulario(request):

    if request.method == 'POST':

        miFormulario= ClaseFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            curso =  Clase(nivel=informacion['nivel'], dias=informacion['dias'])

            curso.save()

            return render(request, "appmwr/inicio.html")

   
    else:
        mi_formulario = ClaseFormulario()

    return render(request, "appmwr/claseFormulario.html", {"mi_formulario": mi_formulario})


def alumnoFormulario(request):

    if request.method == 'POST':

        miFormulario= AlumnoFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            curso =  Alumno(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

            curso.save()

            return render(request, "appmwr/inicio.html")

   
    else:
        mi_formulario = AlumnoFormulario()

    return render(request, "appmwr/alumnoFormulario.html", {"mi_formulario": mi_formulario})

def profesorFormulario(request):

    if request.method == 'POST':

        miFormulario= ProfesorFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            curso =  Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], nivel=informacion['nivel'])

            curso.save()

            return render(request, "appmwr/inicio.html")

   
    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "appmwr/profesorFormulario.html", {"mi_formulario": mi_formulario})



