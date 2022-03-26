from django.db import models
from applications.departamento.models import Departamento
# Create your models here.
class Skills(models.Model):
    skill = models.CharField('Skills', max_length=50)

    class Meta:
         verbose_name_plural = 'Skill'

    def __str__(self):
         return self.skill

class Empleado(models.Model):
    jobs = (
        ('0','Contable'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Secretario'),
        ('4','Ejecutivo')
    )
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    # full_name = models.CharField('Nombre completo', max_length=120)
    job = models.CharField('Trabajo', max_length=20, choices=jobs)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)

    class Meta:
        verbose_name_plural = 'Workers'

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.job