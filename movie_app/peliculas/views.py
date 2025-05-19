from django.shortcuts import render, redirect
from usuarios.models import Pelicula
# Create your views here.
def all_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/peliculas.html', {"peliculas": peliculas})