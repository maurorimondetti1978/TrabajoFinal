from django.shortcuts import render
from django.http import HttpResponse
from .models import Clase, Profesor, Alumno
from .forms import AlumnoFormulario, ClaseFormulario, ProfesorFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "appmwr/inicio.html")

def clases(request):

    clases=Clase.objects.all()

    return render(request,"appmwr/clases.html", {"clases":clases})

   

def alumnos(request):
    
    alumnos=Alumno.objects.all()

    return render(request,"appmwr/alumnos.html", {"alumnos":alumnos})


def profesores(request):

    profesores=Profesor.objects.all()

    return render(request,"appmwr/profesores.html", {"profesores":profesores})


def leerClases(request):

    clases=Clase.objects.all()

    return render(request, "appmwr/leerclases.html", {"clases":clases})


def leerProfesores(request):

    profesores=Profesor.objects.all()

    return render(request, "appmwr/leerprofesores.html", {"profesores":profesores})

def leerAlumnos(request):

    alumnos=Alumno.objects.all()

    return render(request, "appmwr/leeralumnos.html", {"alumnos":alumnos})


def eliminarClases(request, clase_nivel):

    clase=Clase.objects.get(nivel=clase_nivel)
    clase.delete()

    clases= Clase.objects.all()

    return render(request, "appmwr/leerclases.html", {"clases":clases})

def eliminarAlumnos(request, alumno_nombre):

    alumno=Alumno.objects.get(nombre=alumno_nombre)
    alumno.delete()

    alumnos= Alumno.objects.all()

    return render(request, "appmwr/leeralumnos.html", {"alumnos":alumnos})

def eliminarProfesores(request, profesor_nombre):

    profesor=Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores= Profesor.objects.all()

    return render(request, "appmwr/leerprofesores.html", {"profesores":profesores})

def editarClases(request, clase_nivel):

    clase=Clase.objects.get(nivel=clase_nivel)

    if request.method == 'POST':

        miFormulario= ClaseFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            clase.nivel=informacion['nivel']
            clase.dias=informacion['dias']

            clase.save()

            return render(request, "appmwr/inicio.html")

   
    else:
        mi_formulario = ProfesorFormulario(initial={'nivel': clase.nivel, 'dias':clase.dias})

    return render(request, "appmwr/editarClases.html", {"mi_formulario": mi_formulario, "clase_nivel":clase_nivel})

def editarAlumnos(request, alumno_nombre):

    alumno=Alumno.objects.get(nombre=alumno_nombre)

    if request.method == 'POST':

        miFormulario= AlumnoFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            alumno.nombre=informacion['nombre']
            alumno.apellido=informacion['apellido']
            alumno.email=informacion['email']
           

            alumno.save()

            return render(request, "appmwr/inicio.html")

   
    else:
        mi_formulario = AlumnoFormulario(initial={'nombre': alumno.nombre, 'apellido':alumno.apellido, 'email':alumno.email})

    return render(request, "appmwr/editarAlumnos.html", {"mi_formulario": mi_formulario, "alumno_nombre":alumno_nombre})


def editarProfesor(request, profesor_id):

    profesor=Profesor.objects.get(nombre=profesor_id)

    if request.method == 'POST':

        miFormulario= ProfesorFormulario(request.POST)
        
        print(miFormulario)

        if miFormulario.is_valid:

            informacion= miFormulario.cleaned_data

            profesor.nombre=informacion['nombre']
            profesor.apellido=informacion['apellido']
            profesor.nivel=informacion['nivel']

            profesor.save()

            return render(request, "appmwr/inicio.html")

   
    else:
        mi_formulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido, 'nivel':profesor.nivel})

    return render(request, "appmwr/editarProfesor.html", {"mi_formulario": mi_formulario, "profesor_id":profesor_id})
    
def busquedaNivel(request):

    return render(request, 'appmwr/busquedaNivel.html')

def buscar(request):

    respuesta= f" Estoy buscando el niverl: {request.GET['nivel']}"

    return HttpResponse(respuesta)

def buscar(request):
    if request.GET["nivel"]:

        nivel= request.GET['nivel']
        clases= Clase.objects.filter(nivel__icontains=nivel)

        return render(request, 'appmwr/resultadoPorBusquedaNivel.html', {'dias':clases,'nivel':nivel})
    
    else:

        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)


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

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "appmwr/inicio.html", {"mensaje": f"Bienvenido {usuario}"} )
            else:
                return render(request, "appmwr/inicio.html", {"mensaje": "Error, datos incorrectos"})
        
        else:

                return render(request, "appmwr/inicio.html", {"mensaje": "Error, formulario erroneo"})
        

    form = AuthenticationForm()

    return render(request, "appmwr/login.html", {'form':form})

def register(request):

    
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request, "appmwr/inicio.html", {"mensaje": "Usuario Creado:)"})
        
    else:
        form= UserCreationForm()

    return render(request, "appmwr/registro.html" , {"form": form})

def register(request):

    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request, "appmwr/inicio.html", {"mensaje": "Usuario Creado:)"})
        
    else:
        form= UserRegisterForm()

    return render(request, "appmwr/registro.html" , {"form": form})


@login_required
def inicio(request):
    return render(request, "appmwr/inicio.html")

@login_required
def editarPerfil(request):
    
    usuario= request.user

    if request.method == "POST":
        
        miFormulario= UserEditForm(request.POST, request.FILES, instance=request.user)

        if miFormulario.is_valid():

            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen=miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()

            miFormulario.save()

            return render(request, "appmsr/inicio.html")
    
    else:
        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen},instance=request.user)

    return render(request, "appmwr/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'appmwr/cambiarcontrasenia.html'
    success_url = reverse_lazy ('EditarPerfil')





