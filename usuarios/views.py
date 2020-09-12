from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from . import forms

# Create your views here.

def inicio(request):
    context = {'title': 'A Domicilio - Inicio'}
    return render(request, 'base.html', context=context)


def registrar_usuario(request):
    if request.method == 'POST':
        form = forms.RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            authenticate(username=usuario, password=password)
            return redirect('login')
    else:
        form = forms.RegistrarUsuarioForm()
    return render(request, 'usuarios/registrar.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('usuarios:inicio')


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuarios:inicio')
        else:
            context = {'error': 'Verifique el usuario y contraseña que ingresó'}
    elif request.method == "GET":
        context = {}
        form = AuthenticationForm(request)
    if context:
        context.update({'form': form})
    else:
        context = {'form': form}
    return render(request, "usuarios/login.html", context=context)


def register_view(request):
    if request.method == "POST":
        form = forms.RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            authenticate(request, username=username, password=password)
            return redirect('login')
    form = forms.RegistrarUsuarioForm()
    return render(request, 'registration/register.html', {'form': form})

def password_reset_view(request):
    if request.method == "POST":
        pass
