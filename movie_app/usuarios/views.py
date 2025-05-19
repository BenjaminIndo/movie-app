from django.shortcuts import render, redirect
from usuarios.models import Pelicula

def peliculas(request):
    mis_peliculas = Pelicula.objects.all()

    if request.method == "GET":
        return render(request, "usuarios/index.html", {"peliculas": mis_peliculas})
    
    elif request.method == "POST":
        if "addMovie" in request.POST:
            # Agregar nueva película
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
            nueva_pelicula.save()
            if request.user.is_authenticated:
                nueva_pelicula = Pelicula(
                    titulo=titulo,
                    anno=anno,
                    genero=genero,
                    duracion=duracion,
                    director=director,
                    descripcion=descripcion,
                    owner=request.user
                )
            else:
                nueva_pelicula = Pelicula(
                    titulo=titulo,
                    anno=anno,
                    genero=genero,
                    duracion=duracion,
                    director=director,
                    descripcion=descripcion
                )
            nueva_pelicula.save()
        elif "deleteMovie" in request.POST:
            # Eliminar películas seleccionadas
            ids_a_eliminar = request.POST.getlist("checkedbox")
            Pelicula.objects.filter(id__in=ids_a_eliminar).delete()

        return redirect('/')

    # En caso de que no sea ni GET ni POST (por seguridad)
    return redirect('/')
