from django import forms

class AlumnoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()

class ClaseFormulario(forms.Form):
    nivel=forms.CharField(max_length=50)
    dias=forms.CharField(max_length=50)

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    nivel=forms.CharField(max_length=40)
    
    