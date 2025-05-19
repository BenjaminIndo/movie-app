from django.contrib import admin
from account.models import User
from usuarios.models import Pelicula
# Register your models here.
admin.site.register(Pelicula)
admin.site.register(User)

