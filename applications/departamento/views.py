from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import FormView, ListView


from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm

class NewDepartamentoView(FormView):
    template_name = 'new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    #INTERCEPTAMOS EL FORMULARIO
    def form_valid(self, form):
    #CREAMOS EL DEPARTAMENTO CON LOS DATOS DEL FORM
        depart = Departamento(
            name = form.cleaned_data['departamento'],
            iniciales = form.cleaned_data['iniciales']
        )
        depart.save()
    #ASIGNAMOS LOS DATOS DEL FORM A VARIABLES
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
    #CREAMOS EL EMPLEADO
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depart
        )

        return super(NewDepartamentoView, self).form_valid(form)

class ListAllDepartamentosView(ListView):
    template_name = 'list_all_departamentos.html'
    context_object_name = 'departaments'

    def queryset(self):
        key_word = self.request.GET.get('keyWord', '')

        queryset = Departamento.objects.filter(
        name__icontains  = key_word
    )
        return queryset

