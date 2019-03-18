from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm


def home(request):
    return render(request, 'home.html')

def loginUsuario(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form':form}) 

def logoutUsuario(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def passwordUsuario(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            tipo='pos'
            tit='PASSWORD ACTUALIZADO'
            men='El Password ha sido modificado exitosamente.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})          
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/password.html', {'form': form})

def registrarUsuario(request, tipo):
    a=tipo
    if request.method=='POST':  
        user=User.objects.all()
        ban=0
        for u in user:
            if request.POST["username"] == u.username:
                ban=1
        if ban == 0:
            form = UsuarioForm(request.POST)
            if form.is_valid():
                instance=form.save(commit=False)
                Group.objects.get_or_create(name="Jefe")
                Group.objects.get_or_create(name="Oficial")
                if request.user in Group.objects.get(name="Jefe").user_set.all() or request.user.is_superuser:
                    instance.save()
                    if a=='Jefe':
                        user=User.objects.get(username=instance)
                        user.is_staff=True
                        user.groups.add(Group.objects.get(name="Jefe"))
                        user.save()
                        men='El Usuario Gerente ha sido creado exitosamente.'
                    else:
                        user=User.objects.get(username=instance)
                        user.is_staff=True
                        user.groups.add(Group.objects.get(name="Oficial"))
                        user.save()
                        men='El Usuario Staff ha sido creado exitosamente.'
                    tipo='pos'
                    tit='USUARIO CREADO'
                else:
                    tipo='neg'
                    tit='ACCESO DENEGADO'
                    men='No tiene los permisos necesarios para realizar esta tarea.'
                return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
        else:
            tipo='neg'
            tit='USUARIO YA CREADO'
            men='El Usuario ya existe en la base de datos.'
            return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/registro.html', {'form':form})