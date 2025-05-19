from django.shortcuts import render
from django.http import HttpResponseRedirect
from account.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register_user(request):
    if request.method == 'GET':
        # Render the registration form
        return render(request, "account/register.html")
    elif request.method == 'POST':
        nombre = request.POST['username']
        password = request.POST['password']
        mail = request.POST['mail']
        user = User.objects.create_user(username=nombre, password=password, email=mail)
        return HttpResponseRedirect('/')
def login_user(request):
    if request.method == 'GET':
        return render(request, "account/login.html")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['contraseña']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')