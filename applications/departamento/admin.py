from django.contrib import admin
from .models import Departamento
# Register your models here.


class DepartamentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'iniciales',
        'active',
        'id',

    )


admin.site.register(Departamento, DepartamentAdmin)