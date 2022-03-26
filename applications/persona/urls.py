from unicodedata import name
from django.contrib import admin
from django.urls import path

from .import views
from django.urls import path

app_name = 'app_persona'

urlpatterns = [
    path('list-all-workers/', views.ListAllEmpleados.as_view(), name='listWorkers'),
    path('list-all-workers/Admin/', views.ListAllEmpleadosAdmin.as_view(), name='listWorkersAdmin'),
    path('list-by-area/<area>/', views.ListByArea.as_view(), name='listByArea'),
    path('list_by_search/', views.ListWorkersByKey.as_view(), name='listWorker'),
    path('list_skills_worker', views.ListSkillsWorker.as_view()),
    path('worker_info/<pk>/', views.WorkerDetailView.as_view(), name='workerInfo'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('create_worker/', views.WorkerCreateView.as_view(), name='createWorker'),
    path('update_worker/<pk>/', views.WorkerUpdateView.as_view(), name='updateWorker'),
    path('delete_worker/<pk>/', views.WorkerDeleteView.as_view(), name='deleteWorker'),
    path('', views.InicioView.as_view())



]
