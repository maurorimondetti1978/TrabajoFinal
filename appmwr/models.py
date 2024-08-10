from django.db import models

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
        return f"Nombre del Profesor: {self.nombre} - Apellido {self.apellido} - El email es {self.email}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    nivel=models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"Nombre del Profesor: {self.nombre} - Apellido {self.apellido} - El niverl que dicta el Profe: {self.nivel}"

