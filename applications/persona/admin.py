from django.contrib import admin
from .models import Empleado, Skills
# Register your models here.

admin.site.register(Skills)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
        'id'

    )

    def full_name(self,obj):
        return obj.first_name + ' ' + obj.last_name
        
    search_fields = ('first_name',)
    list_filter = ('departamento',)
    filter_horizontal = ('skills',)

admin.site.register(Empleado, EmpleadoAdmin)
