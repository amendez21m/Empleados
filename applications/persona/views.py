from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView

from .models import Empleado


class InicioView(TemplateView):
    # Pagina de inicio
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    template_name = 'list_all_empleados.html'
    # Para paginar
    # paginate_by = 4
    context_object_name = 'workers'
    
    def queryset(self):
        key_word = self.request.GET.get('keyWord', '')
        print(key_word)
        queryset = Empleado.objects.filter(
        first_name__icontains = key_word
    )
        return queryset


class ListAllEmpleadosAdmin(ListView):
    template_name = 'list_all_empleados_admin.html'
    # Para paginar
    # paginate_by = 4
    context_object_name = 'workers'
    model = Empleado


class ListByArea(ListView):
    template_name = 'list_by_area.html'
    context_object_name = 'workers'

    def get_queryset(self):
        #Para recoger el valor de la URL
        area = self.kwargs['area']
       # queryset = super(departamento, self).get_queryset()
        queryset = Empleado.objects.filter(
        departamento__name = area
    )
        return queryset


class ListWorkersByKey(ListView):
    template_name = 'list_by_search.html'
    context_object_name = 'workers'

    def queryset(self):
        key_word = self.request.GET.get('keyWord', '')
        
        queryset = Empleado.objects.filter(
        first_name = key_word
    )
        return queryset

class ListSkillsWorker(ListView):
    template_name = 'list_skills_worker.html'
    context_object_name = 'skills'

    def queryset(self):
        key_word = self.request.GET.get('keyWord', '')
        
        queryset = Empleado.objects.filter(
        id = key_word
    )
       
        return queryset


class WorkerDetailView(DetailView):
    model = Empleado
    context_object_name = 'worker'
    template_name = "worker_info.html"


class SuccessView(TemplateView):
    template_name = "success.html"


class WorkerCreateView(CreateView):
    model = Empleado
    template_name = "create_worker.html"
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'skills']
    fields = ('__all__')
    success_url = reverse_lazy('app_persona:listWorkers')

    # PARA PERSONALIZAR UNA PROPIEDAD DE LA CLASE
   # def form_valid(self,form):
    #    empleado = form.save()
     #   empleado.full_name = empleado.first_name + ' ' + empleado.last_name
     #   empleado.save()
      #  return super(WorkerCreateView, self).form_valid(form)



class WorkerUpdateView(UpdateView):
    model = Empleado
    template_name = "update_worker.html"
    fields = ('__all__')
    success_url = reverse_lazy('app_persona:listWorkers')


class WorkerDeleteView(DeleteView):
    model = Empleado
    context_object_name = 'worker'
    template_name = "delete_worker.html"
    success_url = reverse_lazy('app_persona:listWorkersAdmin')

