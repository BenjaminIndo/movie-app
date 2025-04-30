from django.shortcuts import render, redirect
from usuarios.models import Pelicula
# Create your views here.
def peliculas(request):
    mis_peliculas = Pelicula.objects.all()
    if request.method == "GET":
        return render(request, "usuarios/index.html", {"peliculas":mis_peliculas})
    if request.method =="POST":
        if "addMovie" in request.POST:
            titulo = request.POST["titulo"]
            anno = request.POST["anno"]
            genero = request.POST["genero"]
            duracion = request.POST["duracion"]
            director = request.POST["director"]
            descripcion = request.POST["descripcion"]
            nueva_pelicula = Pelicula(
                titulo=titulo,
                anno=anno,
                genero=genero,
                duracion=duracion,
                director=director,
                descripcion=descripcion
            )
            
            # Guardar la nueva película en la base de datos
            nueva_pelicula.save()
            
            # Redirigir a la misma página para mostrar la lista actualizada de películas
            return redirect('/')  # Asegúrate de que la vista 'peliculas' esté correctamente definida en urls.py
        elif "deleteMovie" in request.POST:
            # Eliminar películas seleccionadas
            ids_a_eliminar = request.POST.getlist("checkedbox")
            Pelicula.objects.filter(id__in=ids_a_eliminar).delete()

        return redirect('/')