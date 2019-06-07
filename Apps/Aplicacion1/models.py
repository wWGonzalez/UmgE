from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Bus(models.Model):
    noBus = models.CharField(max_length=30)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
        #return '%s %s' % (self.nombre, self.carne)

class Estudiante(models.Model):
    carne = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    bus = models.ForeignKey(Bus)

    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  self.nombre
         #return '%s %s' % (self.nombre, self.carne)