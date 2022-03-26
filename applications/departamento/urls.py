from django.contrib import admin
from django.urls import path

from .import views
from django.urls import path

app_name = 'app_departamento'

urlpatterns = [
    path('new_departamento/', views.NewDepartamentoView.as_view(), name='newDepartamento'),
    path('list_all_departamentos/', views.ListAllDepartamentosView.as_view(), name='listDepartamentos')

]
