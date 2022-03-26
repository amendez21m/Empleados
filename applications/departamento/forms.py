from django import forms

#PARA CREAR FORMULARIOS DE DISTINTAS TABLAS

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    iniciales = forms.CharField(max_length=50)