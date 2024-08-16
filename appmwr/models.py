from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Clase(models.Model):
    nivel=models.CharField(max_length=50)
    dias=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Nivel de la clase: {self.nivel} - Dia de la clase {self.dias}"
        
class Alumno(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    

    def __str__(self) -> str:
        return f"Nombre del Alumno: {self.nombre} - Apellido {self.apellido} - El email es {self.email} "

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    nivel=models.CharField(max_length=40)

    def __str__(self)-> str:
        return f"Nombre del Profesor: {self.nombre} - Apellido {self.apellido} - El niverl que dicta el Profe: {self.nivel}"

class Avatar(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__ (self):
        return f"{self.user} - {self.imagen}"