from django.db import models
from account.models import User
class Pelicula(models.Model):
    titulo = models.CharField(max_length=250)
    anno = models.IntegerField(default = 2024)
    genero = models.CharField(max_length=250)
    duracion = models.IntegerField(default = 0)
    director = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
# Create your models here.
