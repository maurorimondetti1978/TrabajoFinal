from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class AlumnoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    nivel=forms.CharField(max_length=40)

class ClaseFormulario(forms.Form):
    nivel=forms.CharField(max_length=50)
    dias=forms.CharField(max_length=50)

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    nivel=forms.CharField(max_length=40)
    
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)  

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        help_text = {k: "" for k in fields} 

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label = "Apellido", required=False)
    first_name= forms.CharField(label ="Nombre", required=False)
    imagen=forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']

class UserRegisterForm(UserCreationForm):

    username= forms.CharField()
    email= forms.EmailField()
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name= forms.CharField()
    first_name= forms.CharField()

    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}