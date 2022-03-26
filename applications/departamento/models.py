from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    iniciales= models.CharField('Iniciales', max_length=20)
    active= models.BooleanField('Activo',default=False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.name
