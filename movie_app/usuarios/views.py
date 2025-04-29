from django.shortcuts import render, redirect
from usuarios.models import Pelicula
# Create your views here.
def peliculas(request):
    mis_peliculas = Pelicula.objects.all()
    return render(request, "usuarios/index.html", {"peliculas":mis_peliculas})
