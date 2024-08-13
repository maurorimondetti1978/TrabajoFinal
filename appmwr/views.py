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
    return render(request, "appmwr/alumnos.html")

def profesores(request):

    profesores=Profesor.objects.all()

    return render(request, "appmwr/profesores.html", {"profesores":profesores})

def busquedaNivel(request):

    return render(request, 'appmwr/busquedaNivel.html')

def buscar(request):

    respuesta= f" Estoy buscando el niverl: {request.GET['nivel']}"

    return HttpResponse(respuesta)

def buscar(request):
    if request.GET["nivel"]:

        nivel= request.GET['nivel']
        dias= Clase.objects.filter(nivel__icontains=nivel)

        return render(request, 'appmwr/resultadosPorBusquedaNivel.html', {'dias':dias,'nivel':nivel})
    
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
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

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
        
        miFormulario= UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():
            miFormulario.save()

            return render(request, "appmsr/inicio.html")
    
    else:
        miFormulario = UserEditForm(instance=request.user)

    return render(request, "appmwr/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'appmwr/cambiarcontrasenia.html'
    success_url = reverse_lazy ('EditarPerfil')





